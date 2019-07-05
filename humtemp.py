import Adafruit_DHT
from time import sleep
sensor=Adafruit_DHT.DHT11
pin=24

while 1:
	humi,temp=Adafruit_DHT.read_retry(sensor ,pin)
	if humi is not None and temp is not None:
		print "Humidity is %d "%humi
		print" temp is %d "%temp


	else:
		print("it not reading is faild")
	sleep(1)