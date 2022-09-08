from urllib import response
from flask import Flask, redirect, url_for, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

dataCenters = requests.get("https://universalis.app/api/v2/data-centers")

print(dataCenters.status_code)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(dataCenters.json())