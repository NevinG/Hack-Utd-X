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
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import json
import pandas as pd
from flask import Flask, request, jsonify
import openai

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
            return {
                "exists": True,
                "user": user
            }
        
        else:
            user = usersRef.document("test").get()
            user = user.to_dict()
            return {
                "exists": True,
                "user": user
            }
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


model = YOLO("yolov8x-seg.pt")  # load instance segmentation model


@app.route("/predict", methods=["POST"])
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

# Load the data
with open('ML/test.json') as f:
    data = json.load(f)

df = pd.json_normalize(data)

def conditionPrediction(data):
    # Decision Tree Algorithm
    # Preprocess the data
    data['built-date'] = pd.to_datetime(data['built-date']).astype(int) / 10**9
    data['defect-log'] = LabelEncoder().fit_transform(data['defect-log'])
    data['maintenance-log'] = LabelEncoder().fit_transform(data['maintenance-log'])
    data['renovation-log'] = LabelEncoder().fit_transform(data['renovation-log'])
    data['roof'] = LabelEncoder().fit_transform(data['roof'])

    # Convert 'condition' from numerical to categorical
    bins = [0, 20, 40, 60, 80, 100]
    labels = ['bad', 'poor', 'moderate', 'good', 'great']
    data['condition'] = pd.cut(data['condition'], bins=bins, labels=labels)

    # Assume 'name' is a column in your data
    if 'name' in data:
        X = data.drop(['condition', 'name'], axis=1)  # Keep name out of features
    else:
        X = data.drop('condition', axis=1)  # No name in the data
        print("Warning: 'name' column not found in the data.")

    y = data['condition']

    # Split the data into training and validation sets
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    # Keep the asset names for the validation set to pair with predictions
    if 'name' in data:
        names_val = data.loc[X_val.index, 'name']

    # Initialize the Decision Tree Classifier
    dt = DecisionTreeClassifier(max_depth=10)

    # Fit the model with the training data
    dt.fit(X_train, y_train)

    # Predict the conditions on the validation set
    predictions = dt.predict(X_val)

    # Evaluate the model
    accuracy = accuracy_score(y_val, predictions)
    print(f'Validation Accuracy: {accuracy}')

    # Pair each prediction with the corresponding asset name
    if 'name' in data:
        prediction_output = pd.DataFrame({
            'Asset Name': names_val,
            'Predicted Condition': predictions
        })
    else:
        prediction_output = pd.DataFrame({
            'Predicted Condition': predictions
        })

    return dt, prediction_output

def valuePredictionOverTime(data):
    # Random Forest Regression
    # Preprocess the data
    data['built-date'] = pd.to_datetime(data['built-date']).astype(int) / 10**9
    data['defect-log'] = LabelEncoder().fit_transform(data['defect-log'])
    data['maintenance-log'] = LabelEncoder().fit_transform(data['maintenance-log'])
    data['renovation-log'] = LabelEncoder().fit_transform(data['renovation-log'])
    data['roof'] = LabelEncoder().fit_transform(data['roof'])

    # Assume 'name' is a column in your data
    if 'name' in data:
        X = data.drop(['value', 'name'], axis=1)  # Keep name out of features
    else:
        X = data.drop('value', axis=1)  # No name in the data
        print("Warning: 'name' column not found in the data.")

    y = data['value']

    # Split the data into training and validation sets
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the Random Forest Regressor
    rf = RandomForestRegressor(n_estimators=100, random_state=42)

    # Fit the model with the training data
    rf.fit(X_train, y_train)

    # Predict the values on the validation set
    predictions = rf.predict(X_val)

    # Evaluate the model
    mse = mean_squared_error(y_val, predictions)
    print(f'Mean Squared Error: {mse}')

    # Pair each prediction with the corresponding asset name
    if 'name' in data:
        prediction_output = pd.DataFrame({
            'Asset Name': data.loc[X_val.index, 'name'],
            'Predicted Value': predictions
        })
    else:
        prediction_output = pd.DataFrame({
            'Predicted Value': predictions
        })

    return rf, prediction_output

openai.api_key = '_____________'

def generate_environmental_report(property):
    # Extract relevant information from the property
    size = property["sq-ft"]
    value = property["value"]
    built_date = property["built-date"]
    renovation_log = property["renovation-log"]
    roof_condition = property["roof"]["condition"]
    roof_type = property["roof"]["type"]
    assets = property["assets"]

    # Prepare the context for the GPT-3 model
    messages = [{"role": "Real Estate Agent", "content":f"The property has a size of {size} square feet and a value of {value}. It was built on {built_date}. The roof condition is rated as {roof_condition} and the roof type is {roof_type}. The renovation log is as follows: {renovation_log}. The assets of the property include: {assets}. Generate an environmental report based off of this context."}]

    # Generate the report using the GPT-3 model
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages,
      temperature=0.5,
      max_tokens=500
    )

    return response.choices[0].text.strip()

def generateNarrative():
    pass


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3030)))
