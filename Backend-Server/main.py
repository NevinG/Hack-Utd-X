#This will be the flask backend server
import os
import firebase_admin
from flask_cors import CORS, cross_origin
from firebase_admin import credentials, firestore, auth

cred = credentials.Certificate("./authenticationKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
usersRef = db.collection("Users")

from flask import Flask, request
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#dict format
testUserData = {
  "assets": [
    {
      "asset_name": "Asset Name",
      "asset_type": "Asset Type",
      "function_type": "exponential",
      "initial_value": 0,
      "min_max_value": 0,
      "r": 0.5,
      "starting_date": "10/21/2023"
    }
  ],
  "bills": [
    {
      "payment_amount": 0,
      "payment_date": "10/21/2023"
    }
  ],
  "checking_account_balance": 0,
  "checking_account_reward": 0,
  "credit_card_balance": 0,
  "credit_card_rewards": 0,
  "deposits": [
    {
      "account": "checkings",
      "amount": 0,
      "date": "10/21/2023"
    }
  ],
  "monthly_bills": [
    {
      "amount": 0
    }
  ],
  "savings_account_balance": 0,
  "savings_account_rewards": 0,
  "withdrawls": [
    {
      "account": "checkings",
      "amount": 0,
      "date": "10/21/2023"
    }
  ]
}

newUserData = {
  "assets": [],
  "bills": [],
  "checking_account_balance": 0,
  "checking_account_reward": 0,
  "credit_card_balance": 0,
  "credit_card_rewards": 0,
  "deposits": [],
  "monthly_bills": [],
  "savings_account_balance": 0,
  "savings_account_rewards": 0,
  "withdrawls": []
}

#Checks if user is authenticated
def check_auth():
    token = request.headers.get("Authtoken", None)
    if token == None:
        return ""
    decoded_token = auth.verify_id_token(token)    
    uid = decoded_token['uid']
    return uid

@app.route('/user', methods=['GET'])
@cross_origin()
def get_user():
    #Add this line to all things
    uid = check_auth()
    if uid == "":
        print("bad uid")
        return {"Error": "Error"}, 400
    
    try:
        #for test just get and print a user
        user = usersRef.document(uid).get()
        if user.exists:
            user = user.to_dict()
            return user
        else:
            user = testUserData
            usersRef.document(uid).set(user)
            return user
    
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

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
