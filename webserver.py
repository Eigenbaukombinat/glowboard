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
        self.respond("""
        <!DOCTYPE html>
<html>
<head>
	<link href='https://fonts.googleapis.com/css?family=Press+Start+2P' rel='stylesheet' type='text/css'>
	<title>KTHXBYE!</title>
</head>
<style>
body {
	text-align:center;
	background-color: #000000;
}
</style>
<body>
    <p class=".text" style="font-family:'Press Start 2P';color:#00ff00;text-align:center;font-size:80px;">KTHXBYE!</p><br/>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <br/>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <br/>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <br/>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <br/>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <br/>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <br/>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <br/>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#00ff00;width:30px;height:30px;display:inline-block;"></div>
    <div style="background-color:#000000;width:30px;height:30px;display:inline-block;"></div>
    <br/>
</body>
</html>
        """)

    def do_GET(self):
        self.respond("""
<!DOCTYPE html><html><head>
<link href='https://fonts.googleapis.com/css?family=Press+Start+2P' rel='stylesheet' type='text/css'>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.2/jquery.min.js"></script>
<script>var init_time = 500;$(document).ready(function() {$('#tt').hide();
$('#tt2').hide();$('.button').hide();$('.text').hide();$('body form').hide();$('#tt').fadeIn(1000);
$('#tt2').delay(init_time).delay(300).fadeIn(150);$('#im_name').delay(init_time).delay(600).fadeIn(150);
$('body form').delay(init_time).delay(450).fadeIn(150);$('#sf').delay(init_time).delay(750).fadeIn(150);
$('#b2').delay(init_time).delay(900).fadeIn(150);});</script><style>body {text-align:center;
background-color: #000000;}#tt {font-family:'Press Start 2P';color:#00ff00;text-align:center;font-size:70px;
margin-bottom:2px;}.text {font-family:'Press Start 2P';color:#00ff00;text-align:center;font-size:20px;
}.button {width: 300px;height: 40px;background-color:#00ff00;border-radius:20px;display:inline-block;}
.button > p {font-family:'Press Start 2P';color:#000000;text-align:center;font-size:20px;margin-top:10px;}
.button:hover {cursor: pointer;}#submit-button {background-color: #00ff00;border: solid;border-radius: 20px;
border-color: #00ff00;width:300px;height:40px;font-family:'Press Start 2P';font-size:20px;
color: #000000;}#submit-button:hover {cursor: pointer;}#select-button {
background-color: #00ff00;border:solid;border-radius: 20px;border-color: #00ff00;width:300px;
height:40px;font-family:'Press Start 2P';font-size:20px;color: #000000;}
#select-button:hover {cursor: pointer;}</style><body><h1 id="tt">Glowboard-Plotter</h1>
<h1 class="text" id="tt2">by EBK/Terminal21</h1><br/><br/><br/>
<form enctype="multipart/form-data" method="post"><p class="text" id="im_name">Image: <br/>
<br/><input type="file" name="file"></p><p><input id="submit-button" type="submit" value="UPLOAD"></p></form></body></html>
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


waiter = 499

while True:
    waiter += 1
    if waiter == 500:
        PLOT_QUEUE.insert(0, '/home/pi/glowboard/doge_glow.jpg')
    if waiter == 1000:
        waiter = 0
        PLOT_QUEUE.insert(0, '/home/pi/glowboard/info.jpg')
    time.sleep(0.3)
    if PLOT_QUEUE:
        plot_image(PLOT_QUEUE.pop())


server.shutdown()
GPIO.cleanup()
