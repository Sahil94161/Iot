import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(24,GPIO.IN)
GPIO.setup(23,GPIO.IN)
while 1:
	try:
		if GPIO.input(24)==0:
			GPIO.output(17,1)
			GPIO.output(27,0)
			GPIO.output(22,1)
			print"1on"
			time.sleep(0.2)
			GPIO.output(22,0)
			GPIO.output(17,1)
			GPIO.output(27,0)
			print"1on"
			time.sleep(0.2)
		elif GPIO.input(23)==0:
			GPIO.output(17,1)
			GPIO.output(27,1)
			GPIO.output(22,0)
			print"2on"
			time.sleep(0.2)
			GPIO.output(22,1)
			GPIO.output(17,0)
			GPIO.output(27,1)
			print"2on"
			time.sleep(0.2)
		else:
			GPIO.output(17,1)
			GPIO.output(27,1)
			GPIO.output(22,1)
			print"off"
			time.sleep(0.2)
			GPIO.output(22,0)
			GPIO.output(17,0)
			GPIO.output(27,0)
			print"off"
			time.sleep(0.2)
	except KeyboardInterrupt:
		 	GPIO.output(17,0)
			GPIO.output(27,0)
			GPIO.output(22,0)