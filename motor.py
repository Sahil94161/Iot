import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
#######################
pin=[17,27,22,5,6,13,19]
for i in range(0,7):
	GPIO.setup(pin[i],GPIO.OUT)
for i in range(0,7):
	GPIO.output(pin[i],0)	
x=GPIO.PWM(17,1000) #1 Khz
x.start(10)
y=GPIO.PWM(22,1000) #1 Khz
y.start(10)
print " hi pwm start with 10%-- duty cycle"
sleep(1)
while 1:
	for i in range(0,100,2):
		print "pwm dutycycle is %d "%i
		sleep(0.2)
		x.ChangeDutyCycle(i)
	for i in range(99,0,-2):
		print "pwm dutycycle is %d "%i
		sleep(0.2)
		x.ChangeDutyCycle(i)
