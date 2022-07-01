# Install these modules
# pip install PyQRCode
# pip install pypng

import pyqrcode
import png
link = "https://www.instagram.com/coding.hubs/"
qr_code = pyqrcode.create(link)
qr_code.png("instagram.png", scale=5)