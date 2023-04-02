import PIL.Image
import PIL.ImageChops
import PIL.ImageDraw
import PIL.ImageFont
import StringIO
import md5
import os
import os.path


DEFAULT_FONT_PATH = 'SourceCodePro-Semibold.ttf'


def hex_to_rgb(hex):
    assert len(hex) == 6
    return tuple(int(hex[pos:pos+2], 16)
            for pos in range(0,6,2))


class FontRegistry(object):
    def __init__(self):
        self.fonts = {}
        self.register_font(DEFAULT_FONT_PATH, 'default')

    def get_font(self, fontname, size):
        fontinfo = self.fonts.get(fontname)
        if fontinfo is None:
            fontinfo = self.fonts['default']
        if size not in fontinfo['sizes'].keys():
            fontinfo['sizes'][size] = PIL.ImageFont.truetype(fontinfo['path'], size)
        return fontinfo['sizes'][size]

    def register_font(self, fontpath, name):
        self.fonts[name] = {'path': fontpath, 'sizes': {}}


class TextImage(object):
    def __init__(self):
        self.registry = FontRegistry()

    def __call__(self, text, canvas_width, fontsize, fontname, color):
        return self.create_image(text.decode('utf8'), canvas_width, fontsize, fontname,
            hex_to_rgb(color))

    def create_image(self, text, canvas_width, fontsize, fontname, color):
        image = PIL.Image.new('RGBA', (canvas_width, 500), (255,255,255,0))
        font = self.registry.get_font(
            fontname, fontsize)
        im = draw_word_wrap(image, text, 0, 0, canvas_width,
            fill=color, font=font)
        data = StringIO.StringIO()
        cropped = im.crop(im.getbbox())
        cropped.save(data, 'PNG')
        return data.getvalue()


def draw_word_wrap(img, text, xpos=0, ypos=0, max_width=130,
                   fill=(0,0,0), font=PIL.ImageFont.load_default()):
    draw = PIL.ImageDraw.Draw(img)
    text_size_x, text_size_y = draw.textsize(text, font=font)
    remaining = max_width
    space_width, space_height = draw.textsize(' ', font=font)
    # use this list as a stack, push/popping each line
    output_text = []
    # split on whitespace...
    for word in text.split():
        word_width, word_height = draw.textsize(word, font=font)
        if word_width + space_width > remaining:
            output_text.append(word)
            remaining = max_width - word_width
        else:
            if not output_text:
                output_text.append(word)
            else:
                output = output_text.pop()
                output += ' %s' % word
                output_text.append(output)
            remaining = remaining - (word_width + space_width)
    alpha = PIL.Image.new('L', img.size, "black")
    image = PIL.Image.new('RGB', img.size, (0,0,0))
    imtext = PIL.Image.new("L", img.size, 0)
    drtext = PIL.ImageDraw.Draw(imtext)
    for text in output_text:
        drtext.text((xpos, ypos), text, font=font, fill='white')
        ypos += text_size_y
    alpha = PIL.ImageChops.lighter(alpha, imtext)
    solidcolor = PIL.Image.new("RGBA", img.size, fill)
    immask = PIL.Image.eval(imtext, lambda p: 255 * (int(p != 0)))
    im = PIL.Image.composite(solidcolor, image, immask)
    im.putalpha(alpha)
    return im


textimage = TextImage()
print textimage(u'09:59', 128, 12, 'default', '000000')
