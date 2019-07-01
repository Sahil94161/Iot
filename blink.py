#!/usr/bin/env python
import Netmaxiot
from time import sleep
arr=[2,3,4,5,6,7]
for i in range (0,6):
	Netmaxiot.pinMode(arr[i],"OUTPUT")		

while 1:
	
	for i in range (0,6):
		Netmaxiot.digitalWrite(arr[i],1)
		print "on"
	sleep(2)
	for i in range (0,6):
		Netmaxiot.digitalWrite(arr[i],0)
		print "off"
	sleep(2)
	