import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)
while(1):
	
	GPIO.output(5,1)
	time.sleep(1)
	GPIO.output(5,0)
	print "led on ho gyi"