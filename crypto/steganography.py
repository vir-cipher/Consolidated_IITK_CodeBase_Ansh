"""
steganography.py - hide a secret message inside a picture (LSB steganography).

the idea i finally got: a pixel is 3 numbers R, G, B (0-255 each). if i flip
ONLY the last (least-significant) bit of a number my eye cant tell the colour
changed, but that bit can secretly carry one bit of my message. spread the
message across loads of pixels and boom - hidden text. took me a while to
believe this actually works lol, but it does.

worked example of the bit trick on ONE colour value:
    red = 150  -> in binary  1001011 0
    message bit to store     = 1
    keep the top 7 bits, force the last bit to my bit:
                             1001011 1  = 151
    150 vs 151 is invisible to the eye, but ive now stored a '1'.

capacity: 3 bits per pixel, 8 bits per character, so a 120x120 image holds
(120*120*3)//8 = 5400 characters. way more than i need for a note.

run order:  make_test_image.py  ->  steganography.py  ->  decode.py
needs Pillow:  pip install pillow
"""
from PIL import Image

MARKER = "1111111111111110"   # 16-bit "STOP" so decode knows where text ends


def encode(img_path, message, out_path="secret.png"):
    """Hide `message` inside the image at `img_path`, save it to `out_path`.

    step by step:
      1. force the image to RGB so every pixel is exactly (r, g, b).
      2. turn the message into bits: each char -> ord() -> 8-bit binary,
         then glue the 16-bit STOP marker on the end.
      3. walk the pixels and drop one message-bit into the last bit of each
         colour value until the bits run out.

    Args:
        img_path: source picture (png recommended).
        message:  the text to hide, e.g. "hello from ansh".
        out_path: where to save the result. MUST stay .png (see warning).

    Example:
        >>> encode("input.png", "meet me at 5")
        done - message hidden inside secret.png
    """
    img = Image.open(img_path).convert("RGB")

    # message -> bits. "Hi" -> 'H'=72=01001000, 'i'=105=01101001, then + MARKER
    bits = ''.join(f"{ord(c):08b}" for c in message) + MARKER

    # (r & ~1) clears the last bit (151 -> 150), then | int(bit) sets it to my
    # message bit. so each colour shifts by at most 1 - invisible to the eye.
    data, out, i = list(img.getdata()), [], 0
    for r, g, b in data:
        if i < len(bits): r = (r & ~1) | int(bits[i]); i += 1
        if i < len(bits): g = (g & ~1) | int(bits[i]); i += 1
        if i < len(bits): b = (b & ~1) | int(bits[i]); i += 1
        out.append((r, g, b))

    # SAVE AS PNG. dont save as jpg!! jpg re-compresses and changes pixels,
    # which wipes my hidden bits (learnt this the annoying way the first time).
    img.putdata(out)
    img.save(out_path)
    print("done - message hidden inside", out_path)


def capacity(img_path):
    """Return how many characters this image can hold (3 bits/pixel / 8)."""
    w, h = Image.open(img_path).size
    return (w * h * 3) // 8


if __name__ == "__main__":
    import os
    # self-contained demo so anyone can just run this file:
    if not os.path.exists("input.png"):
        Image.new("RGB", (120, 120), (128, 128, 128)).save("input.png")
        print("made a test input.png")

    print("this image can hide about", capacity("input.png"), "characters")
    encode("input.png", "hello from ansh")
    print("now run  python decode.py  to read it back out")
    # todo (make it mine): add a password so only the right key reveals the
    # text (xor the message bits with a key before hiding them).
