import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(24,GPIO.IN)
i=0
while 1:
	if GPIO.input(24)==0:
		print"on"
		i=i+1
	if (i==1):

		GPIO.output(17,1)
		GPIO.output(27,1)
	if(i==2):
		GPIO.output(17,0)
		GPIO.output(27,0)
		i=0
		print "off"