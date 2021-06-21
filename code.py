#import smbus
import time
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO


####GPIO setting############

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)

GPIO.setup(7,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

GPIO.output(21,0)
GPIO.output(23,1)

#### setting up MQTT #########

def on_connect(client, userdata, flags, rc):
        print( 'connection made', client, userdata, flags, rc)
        (result, mid) = client.subscribe("paho/prj0108")


def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))
        data = str(msg.payload)
        print(data)
        if(data=='m1'):
                GPIO.output(7,1)
        elif(data=='m0'):
                GPIO.output(7,0)
        elif(data=='b1'):
                GPIO.output(12,1)
        elif(data=='b0'):
                GPIO.output(12,0)
        elif(data=='0'):
                GPIO.output(7,0)
                GPIO.output(12,0)
        elif(data=='1'):
                GPIO.output(7,1)
                GPIO.output(12,1)


mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect("broker.emqx.io", 1883,60)
mqttc.loop_start()


#### Getting the temperature Data #########

#bus = smbus.SMBus(1)

ADDRESS = 0x4B

#def reading1():
 #a= bus.read_byte(ADDRESS)
# return a

while 1:
        input_parameter = GPIO.input(11)
        print(input_parameter)
        (result,mid) = mqttc.publish("paho/temp0108",input_parameter,2)
        time.sleep(2)

#while 1:
#        temp = reading1()
#        temp = float(temp)
#        temperature = ((temp / 256)* 5.13 * 1000/10)
#        temperature = int(temperature)
#        print(temp, temperature)
#
#(result,mid) = mqttc.publish("paho/temp0123",temperature,2)



#mqttc.loop_stop()
#mqttc.disconnect()
mqttc.loop_forever()
