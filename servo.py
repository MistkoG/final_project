#Import library
import RPi.GPIO as GPIO

#Set GPIP mode
GPIO.setmode(GPIO.BOARD)

#Define pin 11 for servo
servoPIN=11

#Set pin as output
GPIO.setup(servoPIN, GPIO.OUT)

#Create instance for PWM @50Hz
pwm=GPIO.PWM(servoPIN,50)

#Start cycle of 7%
pwm.start(7)

#Loop 20x to control the servo position
for i in range(0,20):
	
	#Ask user for position
	desiredPosition=input("where")
	#Calculate the DC(duty cycle) 
	DC=1./18.*(desiredPosition)+2

	# Change the duty cycle of the PWM signal to move the servo
	pwm.ChangeDutyCycle(DC)

# Stop PWM/clean up GPIO settings
pwm.stop()
GPIO.cleanup()
