import json
from flask import Flask
from flask import request
import requests as rqest
import sys
from flask import jsonify
import os
from modules.getThumbnail import getThumbnail


app = Flask(__name__)


@app.route("/getNovel/<novelName>", methods=["POST"])
def getNovel(novelName: str):
    novelName = novelName.lower().replace(" ", "-")
    thumbnail = getThumbnail(novelName)
    return jsonify(
        thumbnail_name=thumbnail
    )


if __name__ == "__main__":
    app.run(host="localhost", port=223)
