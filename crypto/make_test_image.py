# make_test_image.py - just makes a plain input.png so i can test
# encode/decode when i dont have a photo handy. random grey-ish pixels.
from PIL import Image
import random

img = Image.new("RGB", (120, 120))
img.putdata([(random.randint(40, 210),) * 3 for _ in range(120 * 120)])
img.save("input.png")
print("wrote input.png")
