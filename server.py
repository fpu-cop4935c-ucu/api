#!/usr/bin/env python3
import json
from flask import Flask

app = Flask(__name__)

@app.route("/version")
def appinfo():
    with open('appinfo.json') as json_file:
        data = json.load(json_file)
        for p in data['appinfo']:
            return p['version']

if __name__ == '__main__':
    app.run(debug=True)
