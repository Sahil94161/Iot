import time
from Adafruit_IO import Client
from w1thermsensor import W1ThermSensor
import Netmaxiot

#####################################
import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
pin =24
led=0;
sensorValue = 0;
se=W1ThermSensor()
####################################

ADAFRUIT_IO_USERNAME = 'SahilGoyal'
ADAFRUIT_IO_KEY = '65ba9a3ace5a45fd9aabb8083781f856'
#####################################

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

atemp= aio.feeds('hum')
ahum = aio.feeds('temp')
a=aio.feeds('tempe')
b=aio.feeds('light')


while 1:
	hum, tem = Adafruit_DHT.read_retry(sensor, pin)
	x= se.get_temperature()
	sensorValue = Netmaxiot.analogRead(led)
	print("the value from adc is %d"%sensorValue)
	volt=sensorValue*4.887
	print("--------------------------------")
	print("the value of volt is %0.3f"%volt)
	light=volt/5000
	light=light* 100
	print ('light is %d'%light)
	print x
	print light
	print hum
	print tem
	print "---------------------"
	time.sleep(1)
	print "---------------------"
	aio.send(atemp.key, float(tem))
	aio.send(ahum.key, float(hum))
	aio.send(a.key, float(x))
	aio.send(b.key, float(light))

	time.sleep(3)



