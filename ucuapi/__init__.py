from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app) #enables CORS for all routes

# load modules here
from ucuapi.main import main
from ucuapi.addons.service.module import service
from ucuapi.protocols.btle.module import btle
from ucuapi.protocols.zigbee.module import zigbee
from ucuapi.protocols.dummy.module import dummy

# top-level API endpoints
app.register_blueprint(main, url_prefix='/')

# API "addons"
app.register_blueprint(service, url_prefix='/service')

# IoT device Protocol endpoints
app.register_blueprint(btle, url_prefix='/btle')
app.register_blueprint(zigbee, url_prefix='/zigbee')
app.register_blueprint(dummy, url_prefix='/dummy')
