#pip install ubidots
#pip install requests
from ubidots import ApiClient
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

api=ApiClient(token="A1E-uOTLRm4hLfNcgvPaUzm5GDNlBVJSVB")
variable=api.get_variable("5d27093ec03f9777185efc21")

while 1:

    last_value=variable.get_values(1)
    print last_value[0]['value']
    if last_value[0]['value']==1.0:
        
        print "on"
        GPIO.output(17,1)
    else:
        GPIO.output(17,0)
        print "  off"
    time.sleep(0.5)