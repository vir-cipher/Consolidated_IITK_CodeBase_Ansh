# forensics/ — what a photo and a file quietly reveal
- `exif_extract.py` — prints a photo's hidden EXIF data (camera, time, sometimes GPS).
- `integrity_check.py` — SHA-256 fingerprints a folder, then tells you if a file later changed.
Run: `pip install pillow` then `python exif_extract.py` / `python integrity_check.py`.
Make it mine (TODO): a "strip metadata" privacy mode; watch a folder and alert on change.
