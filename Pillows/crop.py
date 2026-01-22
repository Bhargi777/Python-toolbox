from PIL import Image

img = Image.open("input.png")

# (left, upper, right, lower)
cropped = img.crop((100, 100, 400, 400))
cropped.save("cropped.png")

