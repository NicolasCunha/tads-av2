from flask import jsonify

HTTP_OK = 200
HTTP_ERR = 500

def create_response(dict, status):
    response = jsonify(dict, status)
    response.status = status
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response