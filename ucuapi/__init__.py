import json
from flask import Flask

app = Flask(__name__)

@app.route("/version")
def appinfo():
    with open('appinfo.json') as json_file:
        data = json.load(json_file)
        for p in data['appinfo']:
            return p['version']

# load modules here
from ucuapi.protocols.btle.module import btle
from ucuapi.protocols.zigbee.module import zigbee

app.register_blueprint(btle, url_prefix='/btle')
app.register_blueprint(zigbee, url_prefix='/zigbee')
