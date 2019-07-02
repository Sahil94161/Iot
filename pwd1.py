import Netmaxiot
from time import sleep
led=3
led1=5
led2=6
Netmaxiot.pinMode(led,"OUTPUT")
Netmaxiot.pinMode(led1,"OUTPUT")
Netmaxiot.pinMode(led2,"OUTPUT")
sleep(1)
i=0
try:
	Netmaxiot.digitalWrite(led,0)
	Netmaxiot.digitalWrite(led1,0)
	Netmaxiot.digitalWrite(led2,0)
	while 1:
		print(i)
		print("analog pin 3,5,6,9")
		Netmaxiot.analogWrite(led,i)
		Netmaxiot.analogWrite(led1,i)
		Netmaxiot.analogWrite(led2,i)

		i=i+5
		sleep(0.05)
		if(i>255):
			i=0
except KeyboardInterrupt:
	Netmaxiot.digitalWrite(led,0)
	Netmaxiot.digitalWrite(led1,0)
	Netmaxiot.digitalWrite(led2,0)





