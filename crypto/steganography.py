# ============================================================
#  steganography.py  -  hide a secret message inside a picture
#  Hey Ansh - this is your LSB stego tool. Read it top to bottom;
#  every block has a plain-English note above it. You wrote this. :)
# ============================================================
#
#  THE BIG IDEA (one line):
#  A pixel is three numbers - Red, Green, Blue (each 0-255). If you
#  flip only the LAST bit of a number (e.g. 150 -> 151) your eye
#  can't see the change, but that last bit can secretly carry one
#  bit of a message. Do it across many pixels and you've hidden text.
#
#  We use Pillow, the image library:   pip install pillow
from PIL import Image


def encode(img_path, message, out_path="secret.png"):
    # 1) Open the picture and force it into Red/Green/Blue form.
    img = Image.open(img_path).convert("RGB")

    # 2) Turn the message into bits (0s and 1s):
    #    each character -> its number (ord) -> 8 bits.
    #    Then add a 16-bit "STOP HERE" marker so the decoder knows
    #    where the message ends and the random pixels begin.
    bits = ''.join(f"{ord(c):08b}" for c in message) + '1111111111111110'

    # 3) Drop one message-bit into the last bit of each colour value.
    #    (r & ~1) clears the last bit; "| int(bit)" sets it to ours.
    data, out, i = list(img.getdata()), [], 0
    for r, g, b in data:
        if i < len(bits): r = (r & ~1) | int(bits[i]); i += 1
        if i < len(bits): g = (g & ~1) | int(bits[i]); i += 1
        if i < len(bits): b = (b & ~1) | int(bits[i]); i += 1
        out.append((r, g, b))

    # 4) Save as PNG. IMPORTANT: PNG keeps every pixel exactly.
    #    Never save as JPG - it squishes pixels and your hidden
    #    bits get wiped out.
    img.putdata(out)
    img.save(out_path)
    print("Done - your message is hidden inside", out_path)


if __name__ == "__main__":
    # Try it: put an 'input.png' next to this file, then run the script.
    encode("input.png", "hello from ansh")
    # TODO (make it yours): write a decode() that reads the bits back
    # out, and add a password so only the right key reveals the text.
