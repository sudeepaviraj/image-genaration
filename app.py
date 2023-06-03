from flask import Flask,request
from image import create,no_bg,music
import json
import re


app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def hello_world():
    dataset = json.loads(request.data)
    print(dataset["name"])
    return create(dataset["name"])


@app.route("/nobg",methods=['GET', 'POST'])
def nobg():
    dataset = json.loads(request.data)
    print(dataset["image"])
    return no_bg(dataset["image"])

@app.route("/music",methods=['GET', 'POST'])
def musix():
    dataset = json.loads(request.data)
    print(dataset["music"])
    return music(dataset["music"])



if(__name__=="__main__"):
    app.run()