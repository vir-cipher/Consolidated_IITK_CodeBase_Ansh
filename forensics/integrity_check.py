# integrity_check.py - has this file been tampered with?
# a "hash" is like a fingerprint for a file. change even one character and
# the fingerprint changes completely. so i record fingerprints today, then
# re-check later to spot if anything changed. simple but i think its cool.
#
# sha-256 is the fingerprint function. its ONE-WAY: easy to make a print
# from a file, basically impossible to rebuild the file from the print.
# (same idea that protects stored passwords apparently.)
import hashlib, json, os


def sha256(path):
    # read in 8kb chunks (works even for huge files), feed each to the hasher
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def baseline(folder=".", store="baseline.json"):
    # fingerprint every file in the folder once and save the list
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    json.dump({f: sha256(os.path.join(folder, f)) for f in files},
              open(store, "w"), indent=2)
    print("Saved fingerprints for", len(files), "files.")


def check(folder=".", store="baseline.json"):
    # compare todays fingerprints against the saved ones
    for name, saved in json.load(open(store)).items():
        now = sha256(os.path.join(folder, name))
        print(name, "OK" if now == saved else "CHANGED!")


if __name__ == "__main__":
    baseline()   # run once to record
    check()      # now edit a file, run again, watch it say CHANGED!
    # todo (make it mine): keep watching a folder and alert the moment
    # something changes instead of me re-running it by hand.
