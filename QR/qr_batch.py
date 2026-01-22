import qrcode

data_list = [
    "https://google.com",
    "https://github.com",
]

for i, data in enumerate(data_list, start=1):
    img = qrcode.make(data)
    img.save(f"qr_{i}.png")
