import Netmaxiot
from time import sleep


while 1:
	sensorValue =Netmaxiot.analogRead(1)
	print("the value from lm is %d"%sensorValue)
	volt=sensorValue*4.887
	print("--------------------------------")
	print("the value of volt is %0.3f mv"%volt)
	temp=volt/10
	print ('temp is == %0.3f'%temp)
	sleep(1)