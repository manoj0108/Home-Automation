# Home-Automation

There is an increasing demand for smart homes,  where 
appliances react automatically to changing  environmental conditions and can be easily  controlled through one common device.

This project presents a possible solution whereby the user controls devices by using their existing mobile phone where control is communicated to the Microcontroller from a mobile phone through MQTT.

Home automation involves introducing a degree of computerized or automatic control to certain electrical and electronics system in a building.
These involve lighting, temperature control, etc.., this paper demonstrate a simple home automation system which contains a remote mobile host controller and several client module (home appliances).
The client modules communicate with host controllers through internet over the servers available in MQTT.

![1](https://user-images.githubusercontent.com/69961625/122793490-e57ee680-d2d8-11eb-8ea4-8debaf5b76ef.png)


MQTT:

[]MQTT is a lightweight publish/subscribe messaging protocol designed for M2M (machine to machine) telemetry in low bandwidth environments.

[]It was designed by Andy Stanford-Clark (IBM) and Arlen Nipper in 1999 for connecting Oil Pipeline telemetry systems over satellite.

[]There are many MQTT brokers available that you can use for testing and for real applications.


Components:
Raspberry Pi 2
L293d motor driver IC
DC motors(Represents Fan)
Relay
Electric Bulb



The python file is saved in Raspberry Pi (Using VIM editor). The MQTT (MQTT is used for data exchange between constrained devices and server applications) is used to transfer the commands to the Raspberry Pi and also to receive the sensor data continuously from device to Mobile.
