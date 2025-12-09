# Python QR Code

import qrcode

url = input("Enter the URL: ").strip()
file_path = "C:\\Users\\HOME PC\\Desktop\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR Code was generated successfully!")