import Netmaxiot
from time import sleep
button=5
button1=6

led=2
led1=3
led2=4

Netmaxiot.pinMode(button,"INPUT")
Netmaxiot.pinMode(button1,"INPUT")
Netmaxiot.pinMode(led,"OUTPUT")
Netmaxiot.pinMode(led1,"OUTPUT")
Netmaxiot.pinMode(led2,"OUTPUT")
while 1:
	if Netmaxiot.digitalRead(button)==0:
		Netmaxiot.digitalWrite(led,1)
		Netmaxiot.digitalWrite(led1,1)
		Netmaxiot.digitalWrite(led2,1)
		sleep(0.1)
		print"1 on"
		
		Netmaxiot.digitalWrite(led,0)
		Netmaxiot.digitalWrite(led1,0)
		Netmaxiot.digitalWrite(led2,0)
		sleep(0.1)

	elif Netmaxiot.digitalRead(button1)==0:
		Netmaxiot.digitalWrite(led,1)
		Netmaxiot.digitalWrite(led1,0)
		Netmaxiot.digitalWrite(led2,1)
		print" 2 on"
		sleep(0.2)
		Netmaxiot.digitalWrite(led,0)
		Netmaxiot.digitalWrite(led1,1)
		Netmaxiot.digitalWrite(led2,0)
		sleep(0.2)

	else:
		Netmaxiot.digitalWrite(led,0)
		Netmaxiot.digitalWrite(led1,0)
		Netmaxiot.digitalWrite(led2,0)
		print"off"
		sleep(1)
	sleep(0.1)