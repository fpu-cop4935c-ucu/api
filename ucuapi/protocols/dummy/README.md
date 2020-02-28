For debugging purposes, the a few dummy devices are added.

To start, scan for devices:

`curl -X GET http://localhost:5000/dummy/scan`

Then you can see all "devices":

`curl -X GET http://localhost:5000/dummy/devices`

and get "device" info:

`curl -X GET http://localhost:5000/dummy/device/dummy1`

and also get individual values of devices:

`curl -X GET http://localhost:5000/dummy/device/dummy1/lightValue`

and set them, too:

`curl -X POST http://localhost:5000/dummy/device/dummy1/lightValue -d "value=75"`
