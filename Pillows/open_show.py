from PIL import Image

img = Image.open("input.png")
img.show()

print(img.size)
print(img.mode)
