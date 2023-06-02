from flask import Flask,request
from image import create
import json

app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def hello_world():
    dataset = json.loads(request.data)
    print(dataset["name"])
    return create(dataset["name"])

if(__name__=="__main__"):
    app.run()