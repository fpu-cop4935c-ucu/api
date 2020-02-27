from flask import Blueprint, request
import json
import csv
import hashlib

CONFIG_FILE = 'ucuapi/addons/service/config.json'
service = Blueprint('service', __name__)

with open(CONFIG_FILE) as json_file:
    config = json.load(json_file)['config'][0]

USERS_DB = 'ucuapi/addons/service/' + config['usersDb']

@service.route('/unlock', methods = ['POST'])
def service_unlock():
    try:
        users = list(csv.reader(open(USERS_DB)))
        service_hash = "X"
        for userline in users:
            # get the hash for only the "service" user
            if userline[1] == "service":
                service_hash = userline[2]
        pin_attempt = request.form.get('pin_attempt')
        hash_object = hashlib.sha256(pin_attempt.encode())
        hex_dig = str(hash_object.hexdigest())
        if hex_dig == service_hash:
            return "true"
        else:
            return "false", 403
    except IOError: # if we cannot find this file
        return "false", 404
    except AttributeError: # if the pin is not provided
        return "false", 403
    return "false", 403
