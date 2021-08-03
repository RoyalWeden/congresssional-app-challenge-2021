from pyqrcode import QRCode
import pyqrcode
import png

msg = {
    'msg': 'stuff here',
    'other msg': 'more stuff here'
}

qr = pyqrcode.create(str(msg), mode='binary')
print(qr)
print(qr.text())
qr.png('qr.png')
qr.show()