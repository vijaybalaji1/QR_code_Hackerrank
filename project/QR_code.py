import pyqrcode

#create url link
Qrstr="https://www.hackerrank.com/profile/vijaybalaji1002"
url=pyqrcode.create(Qrstr)
url.svg('QR.svg',scale=8)