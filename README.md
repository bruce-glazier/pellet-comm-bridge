## About

I developed this software specifically for the "Master Forge 2500-sq ft Pellet Stove with 140-lb Hopper" from Lowes. This stove has an issue where it will randomly shut off with the message "Goodbye" on the display and never turn back on without someone pressing the power button. This is a huge problem if you depend on this stove as your primary heating source.

## What this does?

This project acts as a communications bridge between the (what I'm calling) the action center and the stove. 
**The "action center" can be found here: https://github.com/bruce-glazier/pellet-action-center**

It really is just a Flask app that leverages the TinyTuya library to communicate with the device and exposes that as a REST inteface.

## Setup

This project depends on the TinyTuya library: https://github.com/jasonacox/tinytuya/blob/master/README.md

The README contains information for setting up a Tuya Developer account, linking your device to that account, and generating the information needed to communicate with your stove. It is a fairly extensive process but luckily they've done a great job at documenting it.

After following the above setup instructions, you should have 4 files generated in this repo:

```
devices.json
snapshot.json
tinytuya.json
tuya-raw.json
```

You will then need to update the dev_id and local_key in app.py.

# To install depends
1. pip install flask
2. pip install tinytuya

# To run:
python -m flask run 