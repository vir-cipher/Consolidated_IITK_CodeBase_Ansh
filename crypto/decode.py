"""
decode.py - read the hidden message back out of a stego png (my version).

this undoes steganography.py. the plan:
  1. walk every pixel, grab the LAST bit of R, G and B.
  2. glue all those bits into one long string.
  3. stop at the 16-bit marker that encode() planted.
  4. slice whats left into 8-bit chunks and turn each chunk back into a char.

worked example of reading ONE colour value:
    red = 151 -> binary ...0001 -> last bit = 151 & 1 = 1
    so this colour was carrying a '1'.

needs Pillow:  pip install pillow
"""
from PIL import Image

MARKER = "1111111111111110"   # same STOP marker encode() used


def decode(path="secret.png"):
    """Return the hidden text inside the stego image at `path`.

    Args:
        path: the png produced by steganography.encode().
    Returns:
        the recovered message as a string.
    Example:
        >>> decode("secret.png")
        'hello from ansh'
    """
    img = Image.open(path).convert("RGB")

    # x & 1 keeps only the last bit: 150&1=0, 151&1=1. do it for r, g, b.
    bits = ""
    for r, g, b in img.getdata():
        bits += str(r & 1) + str(g & 1) + str(b & 1)

    end = bits.find(MARKER)        # where the real message stops
    bits = bits[:end]

    # every 8 bits -> one character. "01001000" -> 72 -> 'H'.
    return "".join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))


if __name__ == "__main__":
    print("hidden message:", decode("secret.png"))
    # if this prints garbage, the png probably got re-saved as jpg somewhere
    # and the last bits changed. keep it png end-to-end.
