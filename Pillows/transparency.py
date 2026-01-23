from PIL import Image

img = Image.open("input.jpg").convert("RGBA")
overlay = Image.new("RGBA", img.size, (255, 155, 35, 100))

Image.alpha_composite(img, overlay).save("transparent.png")
