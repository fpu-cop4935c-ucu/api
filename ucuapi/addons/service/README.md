For debugging purposes, the service pin is 1234, and you can unlock
service mode by doing the following:

`curl -X POST http://localhost:5000/service/unlock -d "pin_attempt=1234"`
