from flask import Flask
from image import create

app = Flask(__name__)

@app.route("/")
def hello_world():
    return create("gekk")