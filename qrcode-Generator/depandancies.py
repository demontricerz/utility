import os
modules=['--upgrade pip','pyqrcode','pillow','Image','pypng']
for module in modules:
    os.system("python -m pip install "+module)