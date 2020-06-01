import sys
import pyqrcode
from PIL import Image
st=sys.argv[1]
out=f"output/{st}.png"
qrobj = pyqrcode.create(st)
with open(out, 'wb') as f:
	qrobj.png(f, scale=100,module_color=(0x00, 0x02, 0x72))
img = Image.open(out)
img=img.convert('RGBA')
width, height = img.size
logo_size = width/4
imag = Image.new('RGBA', (width, height))
logo = Image.open('images/logo2.png')
logo=logo.convert('RGBA')
xmin = ymin = int((width / 2) - (logo_size / 2))
xmax = ymax = int((width / 2) + (logo_size / 2))
logo = logo.resize((xmax - xmin, ymax - ymin))
imag.paste(logo, (xmin, ymin, xmax, ymax))
final2 = Image.new("RGBA", img.size)
final2 = Image.alpha_composite(final2, img)
final2 = Image.alpha_composite(final2, imag)
final2.save(out,'PNG')