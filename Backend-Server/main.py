import os
import firebase_admin
from PIL import Image
import io
import base64
import numpy as np
from ultralytics import YOLO
import cv2
from flask_cors import CORS, cross_origin
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
from flask import Flask, request, jsonify
import openai
from apikey import api_key

from firebase_admin import credentials, firestore, auth

cred = credentials.Certificate("./authenticationKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
usersRef = db.collection("users")


app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


# Checks if user is authenticated
def check_auth():
    token = request.headers.get("Authtoken", None)
    if token == None:
        return ""
    decoded_token = auth.verify_id_token(token)
    uid = decoded_token["uid"]
    return uid

def convert_to_timestamp(dates):
    # If the input is a Series, we can directly use it
    if isinstance(dates, pd.Series):
        dates = dates

    # If it's a single value, make it a list
    elif not isinstance(dates, list):
        dates = [dates]

    # Convert to datetime, handling errors by returning NaT
    date_series = pd.to_datetime(dates, errors='coerce', format='%m/%d/%Y')

    # Convert to UNIX timestamp, turning NaT into None
    timestamps = date_series.map(lambda x: x.timestamp() if pd.notnull(x) else None).tolist()

    # If only one date was passed, return a single value instead of a list
    return timestamps[0] if len(timestamps) == 1 else timestamps


def predict_condition(property):
    # Fake data for training the model
    np.random.seed(42)  # For reproducibility
    synthetic_data = pd.DataFrame({
        'built-date': np.random.randint(1970, 2024, 100),  # Random year between 1970 and 2023
        'defect-log': np.random.choice(['none', 'minor', 'major'], 100),
        'maintenance-log': np.random.choice(['none', 'annual', 'biennial'], 100),
        'renovation-log': np.random.choice(['none', 'recent', 'old'], 100),
        'condition': np.random.choice(['bad', 'poor', 'moderate', 'good', 'great'], 100)
    })

    # Split the synthetic data
    X = synthetic_data.drop('condition', axis=1)
    y = synthetic_data['condition']

    # Encode categorical data
    X = pd.get_dummies(X)

    # Initialize the Decision Tree Classifier
    dt = DecisionTreeClassifier(max_depth=10)

    # Train the model
    dt.fit(X, y)

    # Prepare the property for prediction
    property_for_prediction = {
        'built-date': [property.get('built-date', 1980)],  # Default to 1980 if not provided
        'defect-log': [' '.join(entry.get('description', '') for entry in property.get('defect-log', []))],
        'maintenance-log': [' '.join(entry.get('description', '') for entry in property.get('maintenance-log', []))],
        'renovation-log': [' '.join(entry.get('description', '') for entry in property.get('renovation-log', []))],
    }
    property_df = pd.DataFrame(property_for_prediction)
    property_df = pd.get_dummies(property_df)
    
    # Ensure all columns in the trained model are in the dataframe for prediction
    for col in X.columns:
        if col not in property_df:
            property_df[col] = 0
    
    property_df = property_df.reindex(columns=X.columns, fill_value=0)
    
    # Predict the condition
    prediction = dt.predict(property_df)

    return prediction[0]



# You give it a property, it returns the correct value
# valuePredictionOverTime
def predict_value_over_time(property):
    # Fake for training model
    np.random.seed(42)  # For reproducibility
    synthetic_data = pd.DataFrame({
        'built-date': np.random.randint(1970, 2024, 100),  # Random year between 1970 and 2023
        'defect-log': np.random.choice(['none', 'minor', 'major'], 100),
        'maintenance-log': np.random.choice(['none', 'annual', 'biennial'], 100),
        'renovation-log': np.random.choice(['none', 'recent', 'old'], 100),
        'value': np.random.randint(100000, 500000, 100) 
    })

    # Split the synthetic data
    X = synthetic_data.drop('value', axis=1)
    y = synthetic_data['value']

    # Encode categorical data
    X = pd.get_dummies(X)

    # Initialize the Random Forest Regressor
    rf = RandomForestRegressor(n_estimators=100, random_state=42)

    # Train the model
    rf.fit(X, y)

    # Prepare the property for prediction
    property_for_prediction = {
        'built-date': [property.get('built-date', 1980)],  # Default to 1980 if not provided
        'defect-log': [' '.join(entry.get('description', '') for entry in property.get('defect-log', []))],
        'maintenance-log': [' '.join(entry.get('description', '') for entry in property.get('maintenance-log', []))],
        'renovation-log': [' '.join(entry.get('description', '') for entry in property.get('renovation-log', []))],
    }
    property_df = pd.DataFrame(property_for_prediction)
    property_df = pd.get_dummies(property_df)
    
    # Ensure all columns in the trained model are in the dataframe for prediction
   # Ensure all columns in the trained model are in the dataframe for prediction
    for col in X.columns:
        if col not in property_df:
            property_df[col] = 0
    
    property_df = property_df.reindex(columns=X.columns, fill_value=0)
    # Predict the value
    prediction = rf.predict(property_df)
    return prediction[0]


model = YOLO("yolov8x-seg.pt")  # load instance segmentation model


openai.api_key = api_key


def get_environmental_report(property):
    # Extract relevant information from the property
    size = property["sq-ft"]
    value = property["value"]
    built_date = property["built-date"]
    renovation_log = property["renovation-log"]
    assets = property["assets"]

    # Prepare the context for the GPT-3.5-turbo model
    messages = [
        {
            "role": "user",
            "content": f"The property has a size of {size} square feet and a value of {value}. It was built on {built_date}. The renovation log is as follows: {renovation_log}. The assets of the property include: {assets}. Generate a report based off of this context that accurately details the potential environmental impacts on this property.",
        }
    ]    

    # Generate the report using the GPT-3.5-Turbo model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, temperature=0.5, max_tokens=350
    )

    return {"message": response.choices[0].message.content.strip()}



def get_narrative(property):
    size = property["sq-ft"]
    value = property["value"]
    built_date = property["built-date"]
    renovation_log = property["renovation-log"]
    defect_log = property["defect-log"]
    assets = property["assets"]

    # Prepare the context for the GPT-4 model
    messages = [
        {
            "role": "user",
            "content": f"Play the role of a real estate expert to provide insight to real estate professionals. You are assessing the condition of a property, and are helping real estate professionals see how it compares to other properties on the market. Do not mention this. The property has a size of {size} square feet and a value of {value} in dollars. It was built on {built_date}. The renovation log is as follows: {renovation_log}. The assets of the property include: {assets}. The default log is {defect_log}. Generate a narrative that accurately summarizes the condition and how it compares (or would compare) to similar properties on the market",
        }
    ]

    # Generate the report using the GPT-3 model
    response = openai.ChatCompletion.create(
        model="gpt-4", messages=messages, temperature=0.5, max_tokens=500
    )

    return {"message": response.choices[0]['message']['content']}


# Checks if user is authenticated
@app.route("/user", methods=["GET"])
@cross_origin()
def get_user():
    uid = check_auth()
    if uid == "":
        return {"Error": "Error"}, 400

    try:
        # for test just get and print a user
        user = usersRef.document(uid).get()
        if user.exists:
            user = user.to_dict()
            return {"exists": True, "user": user}

        else:
            user = usersRef.document("test").get()
            user = user.to_dict()
            return {"exists": True, "user": user}
    except Exception as error:
        print(error)
        return {"Error": "Error"}, 400


@app.route("/user", methods=["POST", "PUT"])
@cross_origin()
def post_user():
    # Add this line to all things
    uid = check_auth()
    if uid == "":
        return {"Error": "Error"}, 400
    try:
        # check if user already exists
        newUser = request.json
        usersRef.document(uid).set(newUser)
        return newUser

    except Exception as error:
        print(error)
        return {"Error": "Error"}, 400


@app.route("/get_predict_condition", methods=["POST"])
@cross_origin()
def get_predict_condition():
    uid = check_auth()
    if uid == "":
        return {"Error": "Error"}, 400
    try:
        property = request.json
        data = predict_condition(property)
        if isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
            return jsonify(data.to_json())
        else:
        # handle cases where data is not a pandas object, perhaps it's a string message
            return jsonify({"message": data})

    except Exception as error:
        print(error)
        return {"Error": "Error"}, 400


@app.route("/get_predict_value_over_time", methods=["POST"])
@cross_origin()
def get_predict_value_over_time():
    uid = check_auth()
    if uid == "":
        return {"Error": "Error"}, 400
    try:
        property = request.json
        data = predict_value_over_time(property)
        if isinstance(data, pd.DataFrame) or isinstance(data, pd.Series):
            return jsonify(data.to_json())
        else:
        # handle cases where data is not a pandas object, perhaps it's a string message
            return jsonify({"message": data})

    except Exception as error:
        print(error)
        return {"Error": "Error"}, 400


@app.route("/get_environmental_report", methods=["POST"])
@cross_origin()
def get_calculate_environmental_report():
    uid = check_auth()
    if uid == "":
        return {"Error": "Error"}, 400
    try:
        property = request.json
        data = get_environmental_report(property)
        return data

    except Exception as error:
        print(error)
        return {"Error": "Error"}, 400


@app.route("/get_narrative", methods=["POST"])
@cross_origin()
def get_calculate_narrative():
    uid = check_auth()
    if uid == "":
        return {"Error": "Error"}, 400
    try:
        property = request.json
        data = get_narrative(property)
        return data

    except Exception as error:
        print(error)
        return {"Error": "Error"}, 400


@app.route("/predict", methods=["POST"])
@cross_origin()
def predict():
    data = request.get_json(force=True)
    base64_image: str = data["image"]
    split_string = base64_image.split(",")
    image_data = base64.b64decode(split_string[1])
    # print(base64.b64encode(image_data))
    image = Image.open(io.BytesIO(image_data))
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Predict with the model
    results = model(img)  # predict on an image

    # Draw bounding boxes on the image
    for result in results:
        if result.boxes is not None:
            for box in result.boxes:
                cords = box.xyxy[0].tolist()
                cords = [round(x) for x in cords]
                cv2.rectangle(
                    img, (cords[0], cords[1]), (cords[2], cords[3]), (0, 255, 0), 2
                )
                class_id = result.names[box.cls[0].item()]
                conf = round(box.conf[0].item(), 2)
                cv2.putText(
                    img,
                    f"{class_id}: {conf}",
                    (cords[0], cords[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (36, 255, 12),
                    2,
                )

    # Convert the image with bounding boxes to base64
    is_success, buffer = cv2.imencode(".png", img)
    io_buf = io.BytesIO(buffer)
    base64_img = base64.b64encode(io_buf.getvalue()).decode("utf-8")

    return jsonify({"image": split_string[0] + "," + base64_img})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3030)))
