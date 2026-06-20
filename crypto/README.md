# crypto/ — image steganography

Hides a short text message in the least-significant bits of a PNG so the picture looks totally unchanged, then reads it back.

Run:
```
pip install pillow
python make_test_image.py     # makes input.png
python steganography.py       # hides a message -> secret.png
python decode.py              # reads it back out
```

Files:
- `steganography.py` — `encode()` hides a message in the last bits of each pixel.
- `decode.py` — walks the pixels and pulls the message back.
- `make_test_image.py` — makes a throwaway input.png to test with.

Make it mine (todo): add a password, and print how many chars actually fit.
Inspired by github.com/nitiksh/Steganography-with-Python-Programming (my own code).
