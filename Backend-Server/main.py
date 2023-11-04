import os
import firebase_admin
from flask_cors import CORS, cross_origin

from flask import Flask, request


from firebase_admin import credentials, firestore, auth

cred = credentials.Certificate("./authenticationKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


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
    pass
    

@app.route('/user', methods=['POST', 'PUT'])
@cross_origin()
def post_user():
    pass

def conditionPrediction():
    # Decision Tree
    pass

def valuePredictionOverTime():
    # Multiple Linear/Random Forest Regression
    pass

def generateNarrative():
    pass


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
