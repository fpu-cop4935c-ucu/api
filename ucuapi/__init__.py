from flask import Flask

app = Flask(__name__)

# load modules here
from ucuapi.main import main
from ucuapi.addons.service.module import service
from ucuapi.protocols.btle.module import btle
from ucuapi.protocols.zigbee.module import zigbee

# top-level API endpoints
app.register_blueprint(main, url_prefix='/')

# API "addons"
app.register_blueprint(service, url_prefix='/service')

# IoT device Protocol endpoints
app.register_blueprint(btle, url_prefix='/btle')
app.register_blueprint(zigbee, url_prefix='/zigbee')

