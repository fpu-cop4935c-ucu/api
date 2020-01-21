from flask import Blueprint

zigbee = Blueprint('zigbee', __name__)

@zigbee.route('/test')
def zigbee_main():
    return "Main"
