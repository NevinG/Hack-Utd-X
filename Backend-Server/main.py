import os
import firebase_admin
from flask_cors import CORS, cross_origin

from flask import Flask, request


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
        #check if user already exists
        newUser = request.json
        usersRef.document(uid).set(newUser)
        return newUser
    
    except Exception as error:
        print(error)
        return {"Error": "Error"}, 400

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
