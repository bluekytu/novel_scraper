import json
from flask import Flask
from flask import request


app = Flask(__name__)


# Functions

@app.route("/", methods=["POST"])
def hello_world():
    if request.method == "POST":
        return "<p>ASD World</p>"


@app.route("/receiveNovelTitle", methods=["POST"])
def novelTitleRequest():
    if request.method == "POST":
        data = json.loads(request.data)
        return data


@app.route("fetchImage/<novelName>", methods=["POST"])
def fetchImage(novelName):
