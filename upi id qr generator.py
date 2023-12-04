import pyqrcode
import png#upi id
myUPI='myupiid7478828209@upi'
qrcode=pyqrcode.create(myUPI)
qrcode.png("myUPIid.png")
