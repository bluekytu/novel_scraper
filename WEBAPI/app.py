from flask import Flask
from flask import request

app = Flask(__name__)


# Functions

@app.route("/", methods=["POST"])
def hello_world():
    if request.method == "POST":
        return "<p>ASD World</p>"
