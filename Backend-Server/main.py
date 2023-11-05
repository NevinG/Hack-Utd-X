import os
import firebase_admin
from PIL import Image
import io
import base64
import numpy as np
from ultralytics import YOLO
import cv2
from flask_cors import CORS, cross_origin

from flask import Flask, request, jsonify


from firebase_admin import credentials, firestore, auth

cred = credentials.Certificate("./authenticationKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
usersRef = db.collection("users")


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#Checks if user is authenticated
def check_auth():
    token = request.headers.get("Authtoken", None)
    if token == None:
        return ""
    decoded_token = auth.verify_id_token(token)    
    uid = decoded_token['uid']
    return uid

#Checks if user is authenticated
@app.route('/user', methods=['GET'])
@cross_origin()
def get_user():
    uid = check_auth()
    if uid == "":
        return {"Error": "Error"}, 400
    
    try:
        #for test just get and print a user
        user = usersRef.document(uid).get()
        if user.exists:
            user = user.to_dict()
            return {
                "exists": True,
                "user": user
            }
        else:
            return {"exists": False}
    
    except Exception as error:
        print(error)
        return {"Error": "Error"}, 400
    

@app.route('/user', methods=['POST', 'PUT'])
@cross_origin()
def post_user():
    #Add this line to all things
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
    
model = YOLO('yolov8x-seg.pt')  # load instance segmentation model
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    base64_image = data['image']
    image_data = base64.b64decode(base64_image)
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
                cv2.rectangle(img, (cords[0], cords[1]), (cords[2], cords[3]), (0, 255, 0), 2)
                class_id = result.names[box.cls[0].item()]
                conf = round(box.conf[0].item(), 2)
                cv2.putText(img, f'{class_id}: {conf}', (cords[0], cords[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

    # Convert the image with bounding boxes to base64
    is_success, buffer = cv2.imencode(".png", img)
    io_buf = io.BytesIO(buffer)
    base64_img = base64.b64encode(io_buf.getvalue()).decode('utf-8')

    return jsonify({'image': base64_img})

def conditionPrediction():
    # Decision Tree
    pass

def valuePredictionOverTime():
    # Multiple Linear/Random Forest Regression
    pass

def generateNarrative():
    pass


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3030)))
