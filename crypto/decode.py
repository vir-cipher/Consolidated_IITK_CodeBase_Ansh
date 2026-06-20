# decode.py - read the hidden message back out of a stego png. my version.
# just walk every pixel, grab the last bit of R,G,B, glue them into a long
# bit string, stop at the marker encode() added, then turn 8 bits -> 1 char.
from PIL import Image


def decode(path="secret.png"):
    img = Image.open(path).convert("RGB")
    bits = ""
    for r, g, b in img.getdata():
        bits += str(r & 1) + str(g & 1) + str(b & 1)
    end = bits.find("1111111111111110")        # the stop marker from encode()
    bits = bits[:end]
    return "".join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))


if __name__ == "__main__":
    print("hidden message:", decode("secret.png"))
