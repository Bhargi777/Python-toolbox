import qrcode

qr = qrcode.QRCode()
qr.add_data("Bhargiii")
qr.make()

qr.print_ascii(invert=True)
