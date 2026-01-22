import qrcode

colors = [
    ("black", "white"),
    ("blue", "green"),
    ("darkgreen", "red"),
    ("white", "black"),
]

for i, (fill, back) in enumerate(colors, start=1):
    img = qrcode.make(
        "Color Test",
        image_factory=None
    ).convert("RGB")

    img = qrcode.make(
        "Color Test",
        box_size=10,
        border=4,
    )

    img = qrcode.make(
        "Color Test",
        box_size=10,
        border=4,
    )

    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data("Color Test")
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill, back_color=back)
    img.save(f"qr_color_{i}.png")
