from PIL import Image, ImageFilter

img = Image.open("input.jpg")

img.filter(ImageFilter.BLUR).save("blur.jpg")
img.filter(ImageFilter.GaussianBlur(5)).save("gaussian.jpg")
img.filter(ImageFilter.SHARPEN).save("sharpen.jpg")
img.filter(ImageFilter.FIND_EDGES).save("edges.jpg")
