
from flask import Flask, request, jsonify
from flask_cors import CORS
from enum import Enum
import os
from dotenv import load_dotenv
dotenv_path = os.path.abspath(os.path.dirname(__file__))
load_dotenv(dotenv_path)


app = Flask(__name__)
cors = CORS(app)




class Operator(Enum):
    addition = "+"
    subtraction = "-"
    multiplication = "*"


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
    return response

@app.route("/enum", methods=["POST"])
def calc():
    result = 0
    res = request.get_json()
    operation_type = res.get("operation_type")
    x = res["x"]
    y = res.get("y")

    # check if any of the string occurs in operation_type
    if any(x in operation_type for x in ["subtraction", "subtract", "minus", "difference"]):  
        result = x - y
        Operator.value = "subtraction"

    elif any(x in operation_type for x in ["addition", "add", "plus", "join"]):
        result = x + y
        Operator.value = "addition"

    elif any(x in operation_type for x in ["multiplication" , "times", "multiply", "product"]):
        result = x * y
        Operator.value = "multiplication"


    return jsonify({
        "slackUsername": "offisial",
        "result": result,
        "operation_type": Operator.value
    }), 200, {"content-type": "application/json"}

    
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8090, debug=True)