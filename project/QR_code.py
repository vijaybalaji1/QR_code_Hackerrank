import pyqrcode

#create url link
Qrstr="https://leetcode.com/vijaybalaji123/"
url=pyqrcode.create(Qrstr)
url.svg('QR.svg',scale=8)