#!/usr/bin/python
import Adafruit_DHT
import time
import requests
from w1thermsensor import W1ThermSensor
import Netmaxiot

sensor = Adafruit_DHT.DHT11
pin =24
led=0;
sensorValue = 0;
se=W1ThermSensor()
def myfunction():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    x= se.get_temperature()
    x=round(x,2)
    sensorValue =Netmaxiot.analogRead(led)
    print("the value from adc is %d"%sensorValue)
    volt=sensorValue*4.887
    print("--------------------------------")
    print("the value of volt is %0.3f"%volt)
    light=volt/5000
    light=light* 100
    print ('light is %d'%light)
    print x
    print humidity
    print temperature
    time.sleep(3)
    payload = {'mytemp':temperature, 'myhumdity':humidity,'Dht':x,'light':light}
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
