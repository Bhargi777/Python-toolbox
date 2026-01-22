from PIL import Image

img = Image.open("input.png")

resized = img.resize((300, 300))
resized.save("resized.png")

