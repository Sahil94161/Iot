import time
from Adafruit_IO import Client
#####################################
import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
pin =24
####################################

ADAFRUIT_IO_USERNAME = 'SahilGoyal'
ADAFRUIT_IO_KEY = '65ba9a3ace5a45fd9aabb8083781f856'
#####################################

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

atemp= aio.feeds('hum')
ahum = aio.feeds('temp')

while 1:
	hum, tem = Adafruit_DHT.read_retry(sensor, pin)
	print hum
	print tem
	print "---------------------"
	time.sleep(1)
	print "---------------------"
	aio.send(atemp.key, float(tem))
	aio.send(ahum.key, float(hum))
	time.sleep(3)



