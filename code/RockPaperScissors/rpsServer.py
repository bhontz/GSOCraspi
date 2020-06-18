"""
    Rock, Paper, Scissors Server
"""
import json
from random import randint
from flask import Flask, jsonify

rpsServer = ["rock", "paper", "scissors"]

app = Flask(__name__)

@app.route("/rps", methods=["GET"])
def rps():
    response = "{error: 'whoops, something went wrong'}"

    response = jsonify(rpsServer[randint(0,2)])
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


if __name__ == '__main__':
    app.run(debug=True, host="192.168.100.35", port=8080)
    #app.run(port=8080)