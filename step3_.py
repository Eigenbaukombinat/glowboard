#-----------------------------------
# Name: Stepper Motor
#
# Author: matt.hawkins
#
# Created: 11/07/2012
# Copyright: (c) matt.hawkins 2012
#-----------------------------------
#!/usr/bin/env python
 
# Import required libraries
import time
import RPi.GPIO as GPIO
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
GPIO.setup(13,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)


GPIO.output(26, False)
GPIO.output(13, True)
GPIO.output(19, True)


for x in range (0,1000):
   GPIO.output(26, True)
   time.sleep(0.0004)
   GPIO.output(26, False)
   time.sleep(0.0004)

GPIO.output(19, False)
GPIO.cleanup()
