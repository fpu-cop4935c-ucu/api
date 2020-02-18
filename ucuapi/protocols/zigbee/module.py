from flask import Blueprint
from digi.xbee.devices import ZigBeeDevice
import serial
import time
import json

CONFIG_FILE = 'ucuapi/protocols/zigbee/config.json'
zigbee = Blueprint('zigbee', __name__)

with open(CONFIG_FILE) as json_file:
    config = json.load(json_file)['config'][0]

# need to figure out how to change operating mode of the device

device = ZigBeeDevice(config['devicePort'], config['deviceBaudRate'])

@zigbee.route('/device_info')
def zigbee_device_info():
    return device.read_device_info()

@zigbee.route('/broadcast')
def zigbee_broadcast():
    device.open()
    device.send_data_broadcast("Hello XBee World!")
    device.close()
    return "TEST_BROADCAST_OK"

@zigbee.route('/test')
def zigbee_main():
    return "Main"
