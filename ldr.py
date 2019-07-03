import Netmaxiot
from time import sleep
led=0;
sensorValue = 0; 
while 1:
	sensorValue =Netmaxiot.analogRead(led)
	print("the value from adc is %d"%sensorValue)
	volt=sensorValue*4.887
	print("--------------------------------")
	print("the value of volt is %0.3f"%volt)
	light=volt/5000
	light=light* 100
	print ('light is %d'%light)
	sleep(1)