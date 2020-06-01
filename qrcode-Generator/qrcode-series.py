import os
import pyqrcode
from PIL import Image
pre=input('Enter the Prefix Name: ')
strg=int(input('Enter the starting range: '))
edrg=int(input('Enter the Ending range: '))
inc=int(input('Enter the increment: '))
fol=input('Enter the Output folder name: ')
inc= inc if inc>=0 else -inc
os.system(f"mkdir {fol}")
for st in range(strg,edrg+inc,inc): 
    out=f"{fol}/{pre}-{st}.png"
    qrobj = pyqrcode.create(f"{pre}-{st}")
    with open(out, 'wb') as f:
        qrobj.png(f, scale=40,module_color=(0x00, 0x02, 0x72))
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