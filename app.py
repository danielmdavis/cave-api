from flask import Flask
import json

f = open("clean.json")
caves = json.load(f)

app = Flask(__name__)

@app.route("/")
def api():
    return caves