from PIL import Image, ImageEnhance

img = Image.open("input.jpg")

ImageEnhance.Brightness(img).enhance(1.5).save("brightness.jpg")
ImageEnhance.Contrast(img).enhance(1.5).save("contrast.jpg")
ImageEnhance.Sharpness(img).enhance(2.0).save("sharpness.jpg")
