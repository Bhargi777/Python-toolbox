import qrcode

presets = {
    "small": {"box_size": 5, "border": 2},
    "medium": {"box_size": 12, "border": 3},
    "large": {"box_size": 12, "border": 4},
}

for name, config in presets.items():
    qr = qrcode.QRCode(**config)
    qr.add_data("Hello")
    qr.make(fit=True)
    img = qr.make_image()
    img.save(f"qr_{name}.png")
