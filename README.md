# Universal Control Unit - api

## Installing Dependencies
Be sure that `python3` and `python3-pip` and any other dependencies are installed:

`sudo apt install python3 python3-pip libglib2.0-dev`

and be sure that we have the `flask` pip module installed:

`pip3 install flask bluepy digi-xbee`


## Starting the server
We can now start the server by running:

`sudo ./server.py`

(BTLE requires running as root. Yes, I know it's not ideal)
