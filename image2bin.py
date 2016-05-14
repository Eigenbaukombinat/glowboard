from PIL import Image
import RPi.GPIO as GPIO
from max7219.led import matrix
import time


# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
GPIO.setup(13,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(12,GPIO.IN)

GPIO.output(26, False)


direction = True  # True -> nach rechts

#false -> nach links 
GPIO.output(13, direction)


def convert_image(image_path, max_brightness):
    inputimage = Image.open(image_path)
    w,h = inputimage.size
    if (w,h) != (128,64):
         print "Input image must be 128x64 pixels!"
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

def drive_to_next_col():
    pass




cols = []
for x in range(65):
    a = []
    for y in range(x):
        a.append(1)
    for z in range(64-x):
        a.append(0)
    cols.append(a)

cols = convert_image('cat.jpg', 50)

for col in cols:
    print ''.join(['X' if c else ' ' for c in col])


def find_zero():




def drive_to_next_col():
	GPIO.output(19, True)


	for x in range (0,45):
	   GPIO.output(26, True)
	   #time.sleep(0.0004)
	   time.sleep(0.0034)
	   GPIO.output(26, False)
	   #time.sleep(0.0004)
	   time.sleep(0.0034)

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


cntrlr.clear()



GPIO.cleanup()
