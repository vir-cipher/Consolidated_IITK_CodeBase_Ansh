# decode.py - read the hidden message back out of a stego PNG. My version.
from PIL import Image
def decode(path="secret.png"):
    img = Image.open(path).convert("RGB")
    bits = ""
    for r, g, b in img.getdata():
        bits += str(r & 1) + str(g & 1) + str(b & 1)
    end = bits.find("1111111111111110")       # the marker encode() added
    bits = bits[:end]
    return "".join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))
if __name__ == "__main__":
    print("hidden message:", decode("secret.png"))
