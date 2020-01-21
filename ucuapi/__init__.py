from flask import Flask

app = Flask(__name__)

# load modules here
from ucuapi.main import main
from ucuapi.protocols.btle.module import btle
from ucuapi.protocols.zigbee.module import zigbee

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(btle, url_prefix='/btle')
app.register_blueprint(zigbee, url_prefix='/zigbee')

