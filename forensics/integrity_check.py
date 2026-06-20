# ============================================================
#  integrity_check.py  -  has this file been tampered with?
#  Ansh - a "hash" is like a fingerprint for a file. Change even one
#  character and the fingerprint changes completely. We record the
#  fingerprints today, then re-check later to spot any change.
# ============================================================
#  SHA-256 is the fingerprint function. It's ONE-WAY: easy to make a
#  fingerprint from a file, impossible to rebuild the file from the
#  fingerprint. (Same idea that protects stored passwords.)
import hashlib, json, os


def sha256(path):
    # Read the file in 8 KB chunks (works even for huge files) and
    # feed each chunk into the hasher.
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()          # the fingerprint, as text


def baseline(folder=".", store="baseline.json"):
    # Fingerprint every file in the folder once, and save the list.
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    json.dump({f: sha256(os.path.join(folder, f)) for f in files},
              open(store, "w"), indent=2)
    print("Saved fingerprints for", len(files), "files.")


def check(folder=".", store="baseline.json"):
    # Compare today's fingerprints against the saved ones.
    for name, saved in json.load(open(store)).items():
        now = sha256(os.path.join(folder, name))
        print(name, "OK" if now == saved else "CHANGED!")


if __name__ == "__main__":
    baseline()    # run once to record the fingerprints
    check()       # now edit a file, run again, and watch it say CHANGED!
    # TODO (make it yours): keep watching a folder and alert the very
    # moment something changes.
