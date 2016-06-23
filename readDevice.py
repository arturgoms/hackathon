#! /usr/bin/env python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import serial
import json
import time

baud_rate = 9600
obj_door = 0

def read_door(door):
	return door.readline()

def close_door():
	obj_door.close()

if __name__ == '__main__':


	obj_door = serial.Serial('/dev/ttyUSB0', baud_rate)
	time.sleep(1)
	print "Deu"	
	while 1:

        	client = mqtt.Client()
	        client.connect("192.168.1.100", 1883, 60)
        	client.publish("device/1/5", "1")
		print(read_door(obj_door))
