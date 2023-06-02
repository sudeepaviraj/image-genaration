from flask import Flask,request
from image import create,no_bg
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


if(__name__=="__main__"):
    app.run()