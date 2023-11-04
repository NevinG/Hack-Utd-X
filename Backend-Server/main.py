import os
from flask_cors import CORS, cross_origin

from flask import Flask, request
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


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
