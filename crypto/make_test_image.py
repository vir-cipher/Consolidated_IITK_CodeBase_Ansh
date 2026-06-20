# make_test_image.py - create a plain input.png so you can try encode/decode with no photo handy.
from PIL import Image
import random
img = Image.new("RGB", (120, 120))
img.putdata([(random.randint(40,210),)*3 for _ in range(120*120)])
img.save("input.png"); print("wrote input.png")
