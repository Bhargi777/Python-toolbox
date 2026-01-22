from PIL import Image

img = Image.open("input.jpg")
img.convert("RGB").save("output.jpg")
img.convert("L").save("output_gray.png")
