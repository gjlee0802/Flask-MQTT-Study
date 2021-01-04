import paho.mqtt.client as mqtt #import the client
import time

def on_connect(client, userdata, flags, rc):
     global loop_flag
     print("  In on_connect callback ")
     loop_flag=0

broker_address="127.0.0.1" 
print("creating new instance")
client = mqtt.Client("") #create new instance
client.on_connect=on_connect
client.connect(broker_address) #connect to broker
#client.loop_start()

loop_flag=1
counter=0
while loop_flag==1:
     print("waiting for callback to occur ", counter)
     time.sleep(.01)
     counter+=1
client.disconnect()
client.loop_stop()
