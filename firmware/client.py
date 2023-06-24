from PIL import Image


def to_byte(bitlist):
     out = 0
     for bit in bitlist:
         out = (out << 1) | bit
     return out

def convert_image(image_path, max_brightness):
    inputimage = Image.open(image_path)
    w,h = inputimage.size
    if (w,h) not in ((128,64), (256,128)):
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
        for row in range(h):
            pixel = pixels[col,row]
            if max(pixel) >= max_brightness:
                this_col.append(1)
            else:
                this_col.append(0)
        columns.append(this_col)
    return columns, w

def to_hex(byteint):
    he = hex(byteint)
    if len(he) == 3:
        return f'0x0{he[2]}'
    return he


cols, w = convert_image('../old_stuff/snowden_passes_7.jpg', 120)


outcols = []
for col in cols:
    outcol = []
    printcol = ''
    for i in range(8):
        byte = col[i*8:(i*8)+8]
        printcol += ''.join(['X' if b else ' ' for b in byte])
        outcol.append(to_byte(byte))
    print(printcol)
    outcols.append(outcol)

print("const uint8_t initial_bitmap[128][8] = {")
for outcol in outcols:
    hexstr = ', '.join([f'{to_hex(b)}' for b in outcol])
    print("{ " + hexstr + " },")
print("};")


print(w)
