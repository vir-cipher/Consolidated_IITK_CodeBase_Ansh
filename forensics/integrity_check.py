"""
integrity_check.py - has this file been tampered with?

a "hash" is like a fingerprint for a file: feed the bytes through SHA-256 and
you get a fixed 64-character hex string. change even ONE character in the file
and the fingerprint changes completely. so the plan is: record fingerprints
today (the baseline), then re-check later - anything whose fingerprint moved
has been modified. simple, but its the same idea real integrity tools use.

why SHA-256 specifically: its ONE-WAY. easy to make a fingerprint from a file,
basically impossible to go backwards from the fingerprint to the file. (same
reason websites store a hash of your password instead of the password itself.)

worked example: a file containing exactly "hello" always hashes to
2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824.
add one '!' and its a completely different string.
"""
import hashlib, json, os


def sha256(path):
    """Return the SHA-256 hex fingerprint of the file at `path`.

    reads in 8 KB chunks so it works on huge files without loading the whole
    thing into memory at once.
    """
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):   # stop at b"" (EOF)
            h.update(chunk)
    return h.hexdigest()


def baseline(folder=".", store="baseline.json"):
    """Fingerprint every file in `folder` once and save the list to `store`."""
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    json.dump({f: sha256(os.path.join(folder, f)) for f in files},
              open(store, "w"), indent=2)
    print("Saved fingerprints for", len(files), "files.")


def check(folder=".", store="baseline.json"):
    """Compare todays fingerprints in `folder` against the saved `store`.

    prints OK if a file matches the baseline, CHANGED! if its fingerprint moved.
    """
    for name, saved in json.load(open(store)).items():
        now = sha256(os.path.join(folder, name))
        print(name, "OK" if now == saved else "CHANGED!")


if __name__ == "__main__":
    # worked demo you can actually watch happen:
    with open("demo.txt", "w") as f:
        f.write("original contents\n")
    baseline()                        # 1. record fingerprints (incl. demo.txt)
    with open("demo.txt", "a") as f:
        f.write("...sneaky edit\n")   # 2. tamper with one file
    check()                           # 3. demo.txt now prints CHANGED!
    # todo (make it mine): keep watching a folder and alert the moment
    # something changes instead of me re-running check() by hand.
