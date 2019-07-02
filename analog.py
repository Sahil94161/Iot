import Netmaxiot
from time import sleep

while 1:
	read=Netmaxiot.analogRead(0)
	read1=Netmaxiot.analogRead(1)
	read2=Netmaxiot.analogRead(2)
	read3=Netmaxiot.analogRead(3)
	print("the value from adc is %d"%read)
	print("the value from adc1 is %d"%read1)
	print("the value from adc2 is %d"%read2)
	print("the value from adc3 is %d"%read3)
	volt=read*4.887
	volt1=read1*4.887
	volt2=read2*4.887
	volt3=read3*4.887
	print("--------------------------------")
	print("the value of volt is %0.2f"%volt)
	print("the value of volt1 is %0.2f"%volt1)
	print("the value of volt2 is %0.2f"%volt2)
	print("the value of volt3is %0.2f"%volt3)
	sleep(1)