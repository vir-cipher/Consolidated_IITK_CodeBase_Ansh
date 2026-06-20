# Consolidated_IITK_CodeBase_Ansh

Hi, I'm Ansh — The Shriram Millennium School, Noida. ICSE Class X (2024), 88 in Computer Applications, and I did RoboCup Junior in Class X. I've always liked building things way more than memorising them.

I'm pulling all my coding + security stuff into this one repo so it's in one place. I'm honestly pretty early on the security side — this is a beginner's set of small tools I rebuilt to actually understand how they work, not just copy them. All my own code, and all of it runs (I've checked!).

## What's inside

- `crypto/` — LSB image steganography. `steganography.py` hides a message inside a picture, `decode.py` reads it back out. Run `make_test_image.py` first if you don't have a PNG handy.
- `forensics/` — an EXIF metadata reader (reads the hidden info phones stamp into photos) and a SHA-256 file-integrity checker (spots if a file was tampered with).
- `ml-phishing/` — a little scikit-learn decision tree that flags phishing URLs. This one's my favourite. It ships with a small `sample_dataset.csv` so it runs straight away.
- `ctf-writeups/` — where I write up my picoCTF solves as I do them.
- `evidence/` — my ICSE Class X marksheet and my RoboCup Junior certificate.
- `about/` — a bit about me.

I learned each tool from a public tutorial (I credit it in the file) and then rewrote it in my own words so I'd actually get it. Early days — I keep adding to it.

## How to run it / check it works

```
pip install pillow scikit-learn
cd crypto && python make_test_image.py && python steganography.py && python decode.py
cd ../forensics && python integrity_check.py
cd ../ml-phishing && python phishing_decision_tree.py
```

## Handles

My handle is **vir-cipher**. I'm setting up picoCTF / TryHackMe / Boot.dev profiles under it as I build up a track record — until there's actual solves on them, the real stuff to look at is the code and write-ups in here.
