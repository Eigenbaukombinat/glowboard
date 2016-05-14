from PIL import Image
import RPi.GPIO as GPIO
from max7219.led import matrix
import time
import sys
from time import strftime
import os

speedSelected = False
speedForce = 0

try:
	if sys.argv[3] == "forceday":
		speedSelected = True
		speedForce = 0.005
	elif sys.argv[3] == "forcenight":
		speedSelected = True
		speedForce = 0.001
except:
	pass

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
GPIO.setup(13,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)

GPIO.output(26, False)


directions = {
	"r":True,
	"l":False
}


def speedSelect():
	if speedSelected == True:
		return speedForce
	else:
		if strftime("%p") == "AM":
			if int(strftime("%H")) < 6:
				return 0.001
			else:
				return 0.005
		else:
			if int(strftime("%H")) >= 20:
				return 0.001
			else:
				return 0.005

direction = directions[sys.argv[2]]  # True -> nach rechts

#false -> nach links 
GPIO.output(13, direction)


def convert_image(image_path, max_brightness):
    inputimage = Image.open(image_path)
    w,h = inputimage.size
    if (w,h) != (128,64):
         print "Input image must be 128x64 pixels!"
         exit()
    pixels = inputimage.load()
    columns = []
    for col in range(128):
        this_col = [] 
        if not direction:
            col = 127 - col
        for row in range(h):
	    pixel = pixels[col,row]
	    if max(pixel) < max_brightness:
                this_col.append(1)
            else:
                this_col.append(0)
        columns.append(this_col)
    return columns



cols = []
for x in range(65):
    a = []
    for y in range(x):
        a.append(1)
    for z in range(64-x):
        a.append(0)
    cols.append(a)

cols = convert_image(sys.argv[1], 50)

for col in cols:
    print ''.join(['X' if c else ' ' for c in col])




def drive_to_next_col():
	GPIO.output(19, True)


	for x in range (0,45):
	   GPIO.output(26, True)
	   time.sleep(speedSelect())
	   #time.sleep(0.005)
	   GPIO.output(26, False)
	   time.sleep(speedSelect())
	   #time.sleep(0.005)

	GPIO.output(19, False)

cntrlr = matrix()
cntrlr.clear()
for col in cols:
    for index, val in enumerate(col):
        cntrlr.pixel(index // 8, 7 - (index % 8), val, False)
    cntrlr.pixel(index // 8, 7 - (index % 8), val, True)
    #time.sleep(0.3)
    #cntrlr.clear()
    drive_to_next_col()

if sys.argv[2] == "r":
	os.system("sudo bin/python CLEANUP_image2bin_.py glowboard_blank.jpg l forcenight") #faehrt wieder nach links
elif sys.argv[2] == "l":
        os.system("sudo bin/python CLEANUP_image2bin_.py glowboard_blank.jpg r forcenight") #faehrt wieder nach rechts

cntrlr.clear()



GPIO.cleanup()

