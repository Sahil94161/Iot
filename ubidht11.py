#!/usr/bin/python
import Adafruit_DHT
import time
import requests
from w1thermsensor import W1ThermSensor

sensor = Adafruit_DHT.DHT11
pin =24
se=W1ThermSensor()
def myfunction():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    x= se.get_temperature()
    x=round(x,2)
    print x
    print humidity
    print temperature
    time.sleep(3)
    payload = {'mytemp':temperature, 'myhumdity':humidity,'Dht':x}
    return payload

while 1:
        try:
            r = requests.post('http://things.ubidots.com/api/v1.6/devices/raspberry/?token=A1E-uOTLRm4hLfNcgvPaUzm5GDNlBVJSVB', data=myfunction())
            print('sending our values to ubi dots ')
            print(myfunction())
        except:
            pass
            print "sadi values ubi dots teh nahin gayi wires check karo"          
        time.sleep(10)
