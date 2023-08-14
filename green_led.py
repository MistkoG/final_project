#! /usr/bin/python

# Import the libraries we need
import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the LED GPIO number
LED = 26

# Set the LED GPIO pin as an output
GPIO.setup(LED, GPIO.OUT)

# Turn the GPIO pin on
GPIO.output(LED,True)

# Wait 5 seconds
time.sleep(1)

# Turn the GPIO pin off
GPIO.output(LED,False)
