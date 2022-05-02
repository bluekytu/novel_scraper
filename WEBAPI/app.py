import json
from flask import Flask
from flask import request
from regex import D
import requests

app = Flask(__name__)


# Functions

@app.route("/", methods=["POST"])
def hello_world():
    if request.method == "POST":
        return "<p>ASD World</p>"


@app.route("/receiveNovelTitle", methods=["POST"])
@app.route("/fetchImage/<novelName>", methods=["POST"])
def fetchImage(novelName):
    req = requests.post(f"http://127.0.0.1:223/getNovel/{novelName}")
    data = req.json()

    return data["thumbnail_name"]
