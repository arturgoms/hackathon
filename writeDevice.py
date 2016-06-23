#! /usr/bin/env python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import serial
import json
import time

baud_rate = 9600
obj_door = 0
data = 0

def on_connect(client, userdata, flags, rc):
	print("Connect: "+str(rc))
	client.subscribe('/device/1/#')

def on_message(client, userdata, msg):
	print(msg.topic+ " " + str(msg.payload))	
	
	id = "0"+msg.topic.split("/")[-1]
       	val = "000"+str(msg.payload)

       	toSend = return_object(data['atuadores'], id)
       	obj_door = serial.Serial('/dev/ttyACM0', baud_rate)
       	time.sleep(2);
	if msg.topic.split("/")[-1] != "5":
       		write_door(obj_door,toSend["identificador"]+val)
	

def write_door(door, val):
	door.write(str(val))

def close_door():
	obj_door.close()

def return_object(data, id):
	for d in data:
		if d['identificador'] == id:
			return(d)		

if __name__ == '__main__':
	
	with open('data.json') as json_data:
		data = json.load(json_data)
	
	
	#SETA VALORES PADRAO
	for atu in data['atuadores']:
         	obj_door = serial.Serial('/dev/ttyACM0', baud_rate)
                time.sleep(2);
		write_door(obj_door,atu["identificador"]+atu["valor"])

	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect("192.168.1.100", 1883, 60)
	client.publish("device/1", json.dumps(data))
	client.loop_forever()
