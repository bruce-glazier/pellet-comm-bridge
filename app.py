import tinytuya
from flask import Flask, request

app = Flask(__name__)

# Connect to Device (This is a Pellet Stove and not an outlet device but we are only using basic status commands anyway.)
d = tinytuya.OutletDevice(
    dev_id='', # Fill in with discovered dev_id 
    address='Auto',      # Or set to 'Auto' to auto-discover IP address
    local_key='', # Fill in with local key
    version=3.3)

d.set_socketPersistent(True)

@app.route("/power")
def get_power():
    try:
         data = d.status()
         dps = data.get('dps', {})
         power = dps.get('1', 'undefined')
         return str(power)
    except ValueError:
        return 'Error in getting power status'
    
@app.route("/current-temp")
def get_temp():
    try:
         data = d.status()
         dps = data.get('dps', {})
         currentTemp = dps.get('107', 'undefined')
         return str(currentTemp)
    except ValueError:
        return ValueError
    
@app.route("/get-target-temp")
def get_target_temp():
    try:
         data = d.status()
         dps = data.get('dps', {})
         targetTemp = dps.get('106', 'undefined')
         return str(targetTemp)
    except ValueError:
        return ValueError
        
@app.route("/power-on")
def set_offtime():
    return d.set_status(True, 1, False)

