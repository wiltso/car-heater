# Raspberry pi GMS car heater


## Requirements
- Raspberry pi
- Any kind of usb GMS module (and a SIM card)
- Relay module


## Setup
- Install all requirements to your env
- Remove the `.template` from the files in the `files` folder
- Add your phone number to `ADMIN_NUMBERS` in `files/constants.json`
- Add the user the will run this program to the dialout group `sudo adduser $USER dialout`


## Running
- Run the `main.py` file and start sending messages to the phone number