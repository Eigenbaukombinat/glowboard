from PIL import Image

orig = Image.open('test.png')
new = Image.new('P', orig.size)
p = [255,255,255]
for x in range(25):
    y = 10*x
    p += [y,y,y]
new.putpalette(p)
new.paste(orig)
new.save('out.gif', transparency=0)
#origP = inp.convert('RGB').convert('P', orig.size, palette=Image.ADAPTIVE, colors=255)
#
#inpP.save('out.gif', transparency = 0, optimize = 1)
