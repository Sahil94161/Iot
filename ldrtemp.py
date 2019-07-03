import Netmaxiot
from time import sleep


while 1:
	read =Netmaxiot.analogRead(0)
	sensorValue =Netmaxiot.analogRead(1)
	print("the value from lm is %d"%sensorValue)
	print("the value from adc is %d"%read)
	volt=read*4.887
	volt1=sensorValue*4.887
	print("--------------------------------")
	print("the value of volt is %0.3f"%volt)
	light=volt/5000
	light=light* 100
	print ('light is %d'%light)
	print("--------------------------------")
	print("the value of volt is %0.3f mv"%volt)
	temp=volt1/10
	print ('temp is == %0.3f'%temp)
	sleep(1)