# import qrcode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode

#string represent the qrcode
s = "https://github.com/salamchy/qrCode"

#generate qrcode
url = pyqrcode.create(s)

#create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale = 8)

#create and save the png file naming "myqr.png"
url.png("myqr.png", scale = 6)