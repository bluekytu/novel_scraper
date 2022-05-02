import json
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("getNovel/<novelName>", methods=["POST"])
def getNovel(novelName):
