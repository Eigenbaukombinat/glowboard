import RPi.GPIO as GPIO
import time

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
GPIO.setup(12,GPIO.IN)



while True:
    print GPIO.input(12)
    time.sleep(0.1)



