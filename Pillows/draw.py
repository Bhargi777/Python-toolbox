from PIL import Image, ImageDraw, ImageFont

img = Image.open("input.jpg")
draw = ImageDraw.Draw(img)

text = "Hello people"
position = (50, 50)
color = "powderblue"


font = ImageFont.truetype("/Library/Fonts/constan.ttf", size=48)

draw.text(position, text, fill=color, font=font)
img.save("text_image.jpg")
