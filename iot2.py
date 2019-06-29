import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pin=[17,27,22,5,6,13,19]
#setup mode is on
for i in range(0,7):
	GPIO.setup(pin[i],GPIO.OUT)
	print pin[i]

# used in pins 

while True:
	for i in range(0,7):
		GPIO.output(pin[i],1)
		print "led  %d ON" %i
		print i
		time.sleep(0.3)
		GPIO.output(pin[i],0)
		print "led is off"
		time.sleep(0.3)
	for i in range(6,-1,-1):
		GPIO.output(pin[i],1)
		print "led  %d ON" %i
		print i
		time.sleep(0.3)
		GPIO.output(pin[i],0)
		print "led is off"
		time.sleep(0.3)



