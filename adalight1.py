import time
import Netmaxiot
from Adafruit_IO import Client
DELAY_TIME = 3
ADAFRUIT_IO_USERNAME = 'SahilGoyal'
ADAFRUIT_IO_KEY = '65ba9a3ace5a45fd9aabb8083781f856'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
xlight = aio.feeds('light')
x1light = aio.feeds('light1')
x2light = aio.feeds('light2')
Netmaxiot.pinMode(2,"OUTPUT")
Netmaxiot.pinMode(3,"OUTPUT")
Netmaxiot.pinMode(4,"OUTPUT")
while True:
	mylightdata = aio.receive(xlight.key)
	print('Light', mylightdata.value)
	mylightdata1 = aio.receive(x1light.key)
	print('Light1', mylightdata1.value)
	mylightdata2 = aio.receive(x2light.key)
	print('Light2', mylightdata2.value)

	time.sleep(3)
	x=mylightdata.value
	x=int(x)
	x1=mylightdata1.value
	x1=int(x1)
	x2=mylightdata2.value
	x2=int(x2)
	if x==1:
		print x
		Netmaxiot.digitalWrite(2,1)
	elif(x==0):
		print x
		Netmaxiot.digitalWrite(2,0)
	if x1==1:
		print x1
		Netmaxiot.digitalWrite(3,1)
	elif(x1==0):
		print x1
		Netmaxiot.digitalWrite(3,0)
	if x2==1:
		print x2
		Netmaxiot.digitalWrite(4,1)
	elif(x2==0):
		print x2
		Netmaxiot.digitalWrite(4,0)
	else:
		print(x)
		Netmaxiot.digitalWrite(2,0)
		Netmaxiot.digitalWrite(3,0)
		Netmaxiot.digitalWrite(4,0)