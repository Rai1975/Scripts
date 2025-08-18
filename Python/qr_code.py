import qrcode
import os

# Data to encode
data = input(str('Please enter the link: '))

# Generate QR code
qr = qrcode.QRCode(
    version=1,  #
    error_correction=qrcode.constants.ERROR_CORRECT_H,  
    box_size=10,  
    border=2,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("qrcode.png")

print(f"QR code generated and saved as 'qrcode.png'")
