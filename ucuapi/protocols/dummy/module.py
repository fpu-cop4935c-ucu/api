from flask import Blueprint, request
import json

CONFIG_FILE = 'ucuapi/protocols/dummy/config.json'
dummy = Blueprint('dummy', __name__)

with open(CONFIG_FILE) as json_file:
    config = json.load(json_file)['config'][0]

class Device:
  def __init__(self, udid, devType, values):
    self.udid = udid
    self.devType = devType
    self.values = values

  def setValue(self, name, value):
    self.values[name] = value
  def setType(self, name, devType):
    self.devType[name] = devType

devices = []

@dummy.route('/scan')
def dummy_scan():
    global devices
    devices = []
    # populate the devices list with some dummy devices
    devices.append(Device("dummy0", "lock", {"isLocked": "false"}))
    devices.append(Device("dummy1", "light", {"lightValue": "50"}))
    devices.append(Device("dummy2", "volume", {"volumeLevel": "50"}))
    return "OK"

@dummy.route('/devices')
def dummy_devices():
    data = []
    for dev in devices:
        device = {}
        device["udid"] = dev.udid
        device["devType"] = dev.devType
        device["values"] = dev.values
        data.append(device)
    return jsonify(data)

@dummy.route('/device/<udid>')
def dummy_device(udid):
    data = []
    for dev in devices:
        if dev.udid == udid:
            device = {}
            device["udid"] = dev.udid
            device["devType"] = dev.devType
            device["values"] = dev.values
            data.append(device)
            return json.dumps(data)
    return "ERR", 404 #device not found

@dummy.route('/device/<udid>/<value>', methods = ['GET', 'POST'])
def dummy_device_value(udid, value):
    if request.method == 'GET':
        for dev in devices:
            if dev.udid == udid:
                return str(dev.values[value])
        # device not found
        return "ERR", 404
    elif request.method == 'POST':
        for dev in devices:
            if dev.udid == udid:
                dev.values[value] = request.form.get('value')
                return "OK", 200
        # device not found
        return "ERR", 404
