from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import cgi
import threading
import time
from PIL import Image
import RPi.GPIO as GPIO
from max7219.led import matrix
import time
import sys

FAST = 0.001
SLOW = 0.006
SUPERSLOW = 0.009

GPIO.setmode(GPIO.BCM)

# DIR pin of DRV8825 
GPIO.setup(13,GPIO.OUT)

# STP pin of DRV8825
GPIO.setup(26,GPIO.OUT)

# ENA pin of DRV8825
GPIO.setup(19,GPIO.OUT)

#limit switch
GPIO.setup(12,GPIO.IN)

GPIO.output(26, False)


CUR_DIR = True  # True -> nach rechts
GPIO.output(13, CUR_DIR)

cntrlr = matrix()
cntrlr.brightness(15)


def limit_reached():
    """return true if the limit is reached"""
    return not GPIO.input(12)


def set_direction(direction):
    global CUR_DIR
    ldir = direction.lower()
    if ldir == 'r':
        CUR_DIR = True
    elif ldir == 'l':
        CUR_DIR = False
    else:
        print "FATAL ERROR: Direction %s not valid"
        sys.exit(0)
    GPIO.output(13, CUR_DIR)


def find_limit():
    GPIO.output(19, True)
    if limit_reached():
        print "Limit switch active, moving right a bit and trying again now."
        set_direction('r')
        for x in range(50):
            single_step(SUPERSLOW)
        if limit_reached():
            print "LIMIT SWITCH STILL ACTIVE, SOMETHING WENT WRONG!"
            sys.exit(0)
    set_direction('l')
    while not limit_reached():
        single_step(SUPERSLOW)
    # a few more steps, to measure exactness
    for x in range(5):
        single_step(SUPERSLOW)
    set_direction('r')
    rsteps = 0
    while limit_reached():
        single_step(SUPERSLOW)
        rsteps += 1
    print "limit found. %i steps expected, %i steps got." % (5, rsteps)
    # drive to first column position
    for x in range(30):
        single_step(SLOW)
    GPIO.output(19, False)


def toggle_direction():
    global CUR_DIR
    CUR_DIR = not CUR_DIR
    if CUR_DIR:
        # new dir is right, re-find limit
        find_limit()
    GPIO.output(13, CUR_DIR)


def convert_image(image_path, max_brightness):
    global CUR_DIR
    inputimage = Image.open(image_path)
    w,h = inputimage.size
    if (w,h) != (128,64):
         print "Input image must be 128x64 pixels!"
         return None
    pixels = inputimage.load()
    columns = []
    for col in range(128):
        this_col = [] 
        if not CUR_DIR:
            col = 127 - col
        for row in range(h):
	    pixel = pixels[col,row]
	    if max(pixel) < max_brightness:
                this_col.append(1)
            else:
                this_col.append(0)
        columns.append(this_col)
    return columns




def single_step(speed):
    GPIO.output(26, True)
    time.sleep(speed)
    GPIO.output(26, False)
    time.sleep(speed)


def drive_to_next_col():
    for x in range (0,46):
        single_step(FAST)

cntrlr.clear()
PLOT_QUEUE = []

class GlowImageHandler(BaseHTTPRequestHandler):
    def do_POST(self):

        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        filename = form['file'].filename
        data = form['file'].file.read()
        fn = "/tmp/%s"%filename
        with open(fn, "wb") as imagefile:
            imagefile.write(data)
        PLOT_QUEUE.insert(0, fn)
        self.respond("<html><body><h1>KTHXBYE</h1></body></html>")

    def do_GET(self):
        self.respond("""
        <html><body>
        <form enctype="multipart/form-data" method="post">
        <p>Image: <input type="file" name="file"></p>
        <p><input type="submit" value="Upload"></p>
        </form>
        </body></html>
        """)

    def respond(self, response, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-length", len(response))
        self.end_headers()
        self.wfile.write(response)

server = HTTPServer(('', 9027), GlowImageHandler)
thread = threading.Thread(target=server.serve_forever)
thread.daemon = True
thread.start()

def plot_image(fn):
    #precalc
    cols = convert_image(fn, 50)
    if cols is None:
        print "Bad format!"
        return
    precalced_cols = []
    for col in cols:
        thisprecalced_col = []
        for index, val in enumerate(col):
            thisprecalced_col.append((index // 8, 7- (index % 8), val))
        precalced_cols.append(thisprecalced_col)
    GPIO.output(19, True)
    global CUR_DIR
    print "Plotting", fn
    cntrlr.clear()
    for col in precalced_cols:
        for x, y, val in col:
            cntrlr.pixel(x, y, val, False)
        cntrlr.pixel(x, y, val, True)
        #time.sleep(0.1)
        #cntrlr.clear()
        drive_to_next_col()
    cntrlr.clear()
    toggle_direction()
    GPIO.output(19, False)


find_limit()

print "Listening on port 9027!"


while True:
    time.sleep(0.3)
    if PLOT_QUEUE:
        plot_image(PLOT_QUEUE.pop())




server.shutdown()



GPIO.cleanup()
