from w1thermsensor import W1ThermSensor
from time import sleep
while 1:

	se=W1ThermSensor()
	x= se.get_temperature()
	x=round(x,2)
	print x
	sleep(1)