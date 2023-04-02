from http.server import BaseHTTPRequestHandler,HTTPServer
from luma.led_matrix.device import max7219

from PIL import Image
import cgi
import os
import random
import re
import RPi.GPIO as GPIO
import sys
import threading
import time
import time


FAST = 0.001
SLOW = 0.006
SUPERSLOW = 0.009
IMGPATH = '/home/pi/glowboard'
IMGPATH = '.'


POOL_PASSES = [
    '/home/pi/glowboard/%s' % fn
    for fn in os.listdir(IMGPATH)
    if fn.endswith('.jpg') and 'passes' in fn]

POOL_MONO = [
    '/home/pi/glowboard/%s' % fn
    for fn in os.listdir(IMGPATH)
    if fn.endswith('.jpg') and 'passes' not in fn]

print( "Found %s multipass images in pool." % len(POOL_PASSES))
print( "Found %s mono images in pool." % len(POOL_MONO))


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

cntrlr = max7219()
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
        print( "FATAL ERROR: Direction %s not valid")
        sys.exit(0)
    GPIO.output(13, CUR_DIR)


def find_limit():
    GPIO.output(19, True)
    if limit_reached():
        print( "Limit switch active, moving right a bit and trying again now.")
        set_direction('r')
        for x in range(50):
            single_step(SUPERSLOW)
        if limit_reached():
            print( "LIMIT SWITCH STILL ACTIVE, SOMETHING WENT WRONG!")
            sys.exit(0)
    # drive to the left until limit switch collision is detected
    set_direction('l')
    while not limit_reached():
        single_step(FAST)
    # a few more steps, to measure exactness
    for x in range(5):
        single_step(SUPERSLOW)
    set_direction('r')
    rsteps = 0
    while limit_reached():
        single_step(SUPERSLOW)
        rsteps += 1
    print( "limit found. %i steps expected, %i steps got." % (5, rsteps))
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
    if (w,h) not in  ((128,64), (256,128)):
         print( "Input image must be 128x64 or 256x128 pixels!")
         return None
    if w == 256:
        #scale down to 256x64
        inputimage = inputimage.resize((256,64))
        h = 64
    pixels = inputimage.load()
    columns = []
    for col in range(w):
        this_col = []
        if not CUR_DIR:
            col = w - 1 - col
        for row in range(h):
            pixel = pixels[col,row]
            if max(pixel) >= max_brightness:
                this_col.append(1)
            else:
                this_col.append(0)
        columns.append(this_col)
    return columns, w




def single_step(speed):
    GPIO.output(26, True)
    time.sleep(speed)
    GPIO.output(26, False)
    time.sleep(speed)


def drive_to_next_col(res=128):
    if res == 128:
        steps = 46
    elif res == 256:
        steps = 23
    for x in range (0,steps):
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
        f_passes = form.getvalue('passes')
        try:
            passes = int(f_passes)
        except ValueError:
            passes = 1
        filename = form['file'].filename
        data = form['file'].file.read()
        fn = "/tmp/%s"%filename
        with open(fn, "wb") as imagefile:
            imagefile.write(data)
        PLOT_QUEUE.insert(0, (fn, passes))
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
div.pixel {
    width: 30px;
    height: 30px;
    display: inline-block;
}
div.green {
    background-color: #0f0;
}
div.black {
    background-color: #000;
}
</style>
<body>
    <p class=".text" style="font-family:'Press Start 2P';color:#00ff00;text-align:center;font-size:80px;">KTHXBYE!</p><br/>
    <div class="pixel black"></div>
    <div class="pixel green"></div>
    <div class="pixel green"></div>
    <div class="pixel green"></div>
    <div class="pixel green"></div>
    <div class="pixel green"></div>
    <div class="pixel green"></div>
    <div class="pixel black"></div>
    <br/>
    <div class="pixel green"></div>
    <div class="pixel black"></div>
    <div class="pixel black"></div>
    <div class="pixel black"></div>
    <div class="pixel black"></div>
    <div class="pixel black"></div>
    <div class="pixel black"></div>
    <div class="pixel green"></div>
    <br/>
    <div class="pixel green"></div>
    <div class="pixel black"></div>
    <div class="pixel green"></div>
    <div class="pixel black"></div>
    <div class="pixel black"></div>
    <div class="pixel green"></div>
    <div class="pixel black"></div>
    <div class="pixel green"></div>
    <br/>
    <div class="pixel green"></div>
    <div class="pixel black"></div>
    <div class="pixel black"></div>
    <div class="pixel black"></div>
    <div class="pixel black"></div>
    <div class="pixel black"></div>
    <div class="pixel black"></div>
    <div class="pixel green"></div>
    <br/>
    <div class="pixel green"></div>
    <div class="pixel black"></div>
    <div class="pixel green"></div>
    <div class="pixel black"></div>
    <div class="pixel black"></div>
    <div class="pixel green"></div>
    <div class="pixel black"></div>
    <div class="pixel green"></div>
    <br/>
    <div class="pixel green"></div>
    <div class="pixel black"></div>
    <div class="pixel black"></div>
    <div class="pixel green"></div>
    <div class="pixel green"></div>
    <div class="pixel black"></div>
    <div class="pixel black"></div>
    <div class="pixel green"></div>
    <br/>
    <div class="pixel green"></div>
    <div class="pixel black"></div>
    <div class="pixel black"></div>
    <div class="pixel black"></div>
    <div class="pixel black"></div>
    <div class="pixel black"></div>
    <div class="pixel black"></div>
    <div class="pixel green"></div>
    <br/>
    <div class="pixel black"></div>
    <div class="pixel green"></div>
    <div class="pixel green"></div>
    <div class="pixel green"></div>
    <div class="pixel green"></div>
    <div class="pixel green"></div>
    <div class="pixel green"></div>
    <div class="pixel black"></div>
    <br/>
</body>
</html>
        """)

    def do_GET(self):
        self.respond("""
<!DOCTYPE html>
<html>
<head>
<link href='https://fonts.googleapis.com/css?family=Press+Start+2P' rel='stylesheet' type='text/css'>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.2/jquery.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js"></script>
<style>
body {
text-align:center;
background-color: #000000;
}

#tt {
font-family:'Press Start 2P';
color:#00ff00;
text-align:center;
font-size:70px;
margin-bottom:2px;
}

.text {
font-family:'Press Start 2P';
color:#00ff00;
text-align:center;
font-size:20px;
}

.button {
width: 300px;
height: 40px;
background-color:#00ff00;
border-radius:20px;
display:inline-block;
}

.button > p {
font-family:'Press Start 2P';
color:#000000;
text-align:center;
font-size:20px;
margin-top:10px;
}

.button:hover {
cursor: pointer;
}

#submit-button {
background-color: #00ff00;
border: solid;
border-radius: 20px;
border-color: #00ff00;
width:300px;
height:40px;
font-family:'Press Start 2P';
font-size:20px;
color: #000000;
}

#submit-button:hover {
cursor: pointer;
}

#select-button {
background-color: #00ff00;
border:solid;
border-radius: 20px;
border-color: #00ff00;
width:300px;
height:40px;
font-family:'Press Start 2P';
font-size:20px;
color: #000000;
}

#select-button:hover {
cursor: pointer;
}

.footer {
    margin-bottom: 2px;
    text-align: right;
}

</style>
<script>
var init_time = 500;
$(document).ready(function() {
$('#tt').hide();
$('#tt2').hide();
$('.button').hide();
$('.text').hide();
$('body form').hide();
$('#tt').fadeIn(1000);
$('#tt2').delay(init_time).delay(300).fadeIn(150);
$('p.text').delay(init_time).delay(600).fadeIn(150);
$('body form').delay(init_time).delay(450).fadeIn(150);
$('#sf').delay(init_time).delay(750).fadeIn(150);
$('#b2').delay(init_time).delay(900).fadeIn(150);
$('#info').delay(init_time).delay(1050).fadeIn(150);
$('#info2').delay(init_time).delay(1200).fadeIn(150);
$('#footer').delay(init_time).delay(1500).fadeIn(500);
});
</script>

<body>
<h1 id="tt">Glowboard-Plotter</h1>
<h1 class="text" id="tt2">by EBK/Terminal21</h1>
<br/>
<br/>
<br/>
<form enctype="multipart/form-data" method="post">
<p class="text" id="im_name">Image: <br/>(128x64 or 256x128 RGB-jpeg)<br/>
<input type="file" name="file" />
</p>
<p class="text">Number of passes: <br/><br/>
<input type="text" value="1" size="2" name="passes" />
<p>
<input id="submit-button" type="submit" value="UPLOAD">
</p><br/><br/>
<p class="text" id="info">
Please do only upload .jpg files with a size of 128x64 OR 256x128 pixels!<br/>
</p>
<p class="text" style="text-weight:bold;" id="info2">
Otherwise your image will be ignored.<br/>
</form>
<br/><br/>
<p class="text" style="font-size:10px" id="footer">Main coding: nilo <|> Style of web interface: sesshomariu</p>
</body>
</html>
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

def plot_image(fn, passes):
    print( "plotting %s with %s passes" % (fn, passes))
    if passes > 10:
        passes = 10
    elif passes < 1:
        passes = 1
    precalced_passes = []
    brightness_offset = 0
    increase_per_pass = 240 / float(passes)
    for pass_id in range(passes):
        brightness_offset += increase_per_pass
        brightness_offset = int(brightness_offset)
        #precalc
        cols, res = convert_image(fn, brightness_offset)
        if cols is None:
            print( "Bad format!")
            return
        precalced_cols = []
        for col in cols:
            thisprecalced_col = []
            for index, val in enumerate(col):
                thisprecalced_col.append((index // 8, 7- (index % 8), val))
            precalced_cols.append(thisprecalced_col)
    #plot
    GPIO.output(19, True)
    global CUR_DIR
    cntrlr.clear()
    for col in precalced_cols:
        for x, y, val in col:
            #asdf
            cntrlr.pixel(x, y, val, False)
            cntrlr.pixel(x, y, val, True)
            #time.sleep(0.1)
            #cntrlr.clear()
        drive_to_next_col(res)
    cntrlr.clear()
    toggle_direction()
    GPIO.output(19, False)


find_limit()

print( "Listening on port 9027!")


waiter = 999

while True:
    waiter += 1
    if waiter == 500:
        PLOT_QUEUE.insert(0, ('/home/pi/glowboard/info.jpg', 1))
    if waiter == 1000:
        poolimg = random.choice(POOL_PASSES)
        passes = 1
        passesres = re.findall('passes_([0-9]+)\.jpg', poolimg)
        if len(passesres):
            passes = int(passesres[0])
            PLOT_QUEUE.insert(0, (poolimg, passes))
    if waiter == 1500:
        waiter = 0
        poolimg = random.choice(POOL_MONO)
        PLOT_QUEUE.insert(0, (poolimg, 1))
    time.sleep(0.3)
    if PLOT_QUEUE:
        plot_image(*PLOT_QUEUE.pop())


server.shutdown()
GPIO.cleanup()
