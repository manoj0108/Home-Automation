# Home-Automation

There is an increasing demand for smart homes,  where 
appliances react automatically to changing  environmental conditions and can be easily  controlled through one common device.

This project presents a possible solution whereby the user controls devices by using their existing mobile phone where control is communicated to the Microcontroller from a mobile phone through MQTT.

Home automation involves introducing a degree of computerized or automatic control to certain electrical and electronics system in a building.
These involve lighting, temperature control, etc.., this paper demonstrate a simple home automation system which contains a remote mobile host controller and several client module (home appliances).
The client modules communicate with host controllers through internet over the servers available in MQTT.


Components:
Raspberry Pi 2
L293d motor driver IC
DC motors(Represents Fan)
Relay
Electric Bulb


The python file is saved in Raspberry Pi (Using VIM editor). The MQTT (MQTT is used for data exchange between constrained devices and server applications) is used to transfer the commands to the Raspberry Pi. 
