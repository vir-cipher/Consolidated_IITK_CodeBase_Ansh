"""
make_test_image.py - makes a plain input.png to test encode/decode with.

i dont always have a photo handy, so this paints a 120x120 image of random
grey-ish pixels and saves it as input.png. grey means R=G=B, which makes it
easy to eyeball that hiding a message doesnt visibly change anything.

run this first, then steganography.py, then decode.py.
needs Pillow:  pip install pillow
"""
from PIL import Image
import random

SIZE = 120   # 120x120 = 14400 pixels = room for ~5400 hidden characters


def make(path="input.png"):
    """Write a SIZE x SIZE png of random grey pixels to `path`."""
    img = Image.new("RGB", (SIZE, SIZE))
    # (v, v, v) = grey. v between 40 and 210 so its mid-tone, not pure
    # black/white (pure 0 or 255 has no room to nudge up/down by 1).
    img.putdata([(random.randint(40, 210),) * 3 for _ in range(SIZE * SIZE)])
    img.save(path)
    print("wrote", path, f"({SIZE}x{SIZE})")


if __name__ == "__main__":
    make()
