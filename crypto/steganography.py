# steganography.py - hide a secret message inside a picture
# ok so the idea i finally got: a pixel is 3 numbers R,G,B (0-255 each).
# if i flip ONLY the last bit of a number (150 -> 151) my eye cant tell,
# but that last bit can secretly carry one bit of my message. do it over
# loads of pixels and boom, hidden text. took me a while to believe this
# actually works lol but it does.
#
# needs Pillow:  pip install pillow
from PIL import Image


def encode(img_path, message, out_path="secret.png"):
    # open the pic and force it to RGB
    img = Image.open(img_path).convert("RGB")

    # message -> bits. each char -> its number (ord) -> 8 bits.
    # then a 16-bit STOP marker so decode knows where the message ends
    # and the rest of the random pixels begin.
    bits = ''.join(f"{ord(c):08b}" for c in message) + '1111111111111110'

    # drop one message-bit into the last bit of each colour value.
    # (r & ~1) clears the last bit, then | int(bit) sets it to mine.
    data, out, i = list(img.getdata()), [], 0
    for r, g, b in data:
        if i < len(bits): r = (r & ~1) | int(bits[i]); i += 1
        if i < len(bits): g = (g & ~1) | int(bits[i]); i += 1
        if i < len(bits): b = (b & ~1) | int(bits[i]); i += 1
        out.append((r, g, b))

    # SAVE AS PNG. dont save as jpg!! jpg squishes pixels and wipes my
    # hidden bits (learnt this the annoying way the first time).
    img.putdata(out)
    img.save(out_path)
    print("done - message hidden inside", out_path)


if __name__ == "__main__":
    # try it: put an input.png next to this file then run.
    encode("input.png", "hello from ansh")
    # todo (make it mine): add a password so only the right key reveals
    # the text, and print how many chars actually fit in a given image.
