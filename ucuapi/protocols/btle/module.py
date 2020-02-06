from flask import Blueprint, request
from bluepy.btle import Scanner, DefaultDelegate
import json

CONFIG_FILE = 'ucuapi/protocols/btle/config.json'
btle = Blueprint('btle', __name__)

with open(CONFIG_FILE) as json_file:
    config = json.load(json_file)['config'][0]

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("[btle] Discovered device", dev.addr)
        elif isNewData:
            print("[btle] Received new data from", dev.addr)

scanner = Scanner().withDelegate(ScanDelegate())
devices = {}

@btle.route('/scan')
def btle_scan():
    timeout = request.args.get('timeout', default = config['defaultTimeout'], type = int)
    global devices
    devices = scanner.scan(timeout, passive=True)
    return "OK"

@btle.route('/devices')
def btle_devices():
    data = []
    for dev in devices:
        device = {}
        device["addr"] = dev.addr
        device["addrType"] = dev.addrType
        device["rssi"] = dev.rssi
        data.append(device)
    return json.dumps(data)

