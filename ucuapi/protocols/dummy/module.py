from flask import Blueprint
import json

CONFIG_FILE = 'ucuapi/protocols/dummy/config.json'
dummy = Blueprint('dummy', __name__)

with open(CONFIG_FILE) as json_file:
    config = json.load(json_file)['config'][0]

class Device:
  def __init__(self, udid, values):
    self.udid = udid
    self.values = values

  def setValue(self, name, value):
    self.values[name] = value

devices = []

@dummy.route('/scan')
def dummy_scan():
    global devices
    devices = []
    # populate the devices list with some dummy devices
    devices.append(Device("dummy0", {}))
    devices.append(Device("dummy1", {"lightValue": 50}))
    return "OK"

@dummy.route('/devices')
def dummy_devices():
    data = []
    for dev in devices:
        device = {}
        device["udid"] = dev.udid
        device["values"] = dev.values
        data.append(device)
    return json.dumps(data)

@dummy.route('/device/<udid>')
def dummy_device(udid):
    data = []
    for dev in devices:
        if dev.udid == udid:
            device = {}
            device["udid"] = dev.udid
            device["values"] = dev.values
            data.append(device)
    return json.dumps(data)

@dummy.route('/device/<udid>/<value>', methods = ['GET'])
def dummy_device_value(udid, value):
    data = []
    for dev in devices:
        if dev.udid == udid:
            return str(dev.values[value])

