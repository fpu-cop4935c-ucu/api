from flask import Blueprint
import json

CONFIG_FILE = 'ucuapi/addons/service/config.json'
service = Blueprint('service', __name__)

with open(CONFIG_FILE) as json_file:
    config = json.load(json_file)['config'][0]

@service.route('/unlock')
def service_unlock():
    # TODO: implement hashing and verification here
    return "false", 403
