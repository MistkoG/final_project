import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
servoPIN=11
GPIO.setup(servoPIN, GPIO.OUT)
pwm=GPIO.PWM(servoPIN,50)
pwm.start(7)
for i in range(0,20):
	desiredPosition=input("where")
	DC=1./18.*(desiredPosition)+2
	pwm.ChangeDutyCycle(DC)
pwm.stop()
GPIO.cleanup()
