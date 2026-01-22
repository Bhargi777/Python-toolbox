from PIL import Image

img = Image.open("input.jpg")

rotated = img.rotate(263, expand=True)
rotated.save("rotated.jpg")

flipped_l_r = img.transpose(Image.FLIP_LEFT_RIGHT)
flipped_t_b = img.transpose(Image.FLIP_TOP_BOTTOM)
flipped_l_r.save("flipped_l_r.jpg")
flipped_t_b.save("flipped_t_b.jpg")