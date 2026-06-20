# ============================================================
#  exif_extract.py  -  see what a photo secretly remembers
#  Ansh - phones quietly stamp photos with the camera model, the
#  time, and sometimes the exact GPS spot. This tool reads that back.
# ============================================================
#  Why it matters: post a holiday photo and you might be posting
#  your location too. Spotting this is the first taste of "forensics".
#
#  pip install pillow
from PIL import Image
from PIL.ExifTags import TAGS   # TAGS turns numeric codes into names


def show_exif(path):
    # getexif() gives a dictionary shaped like {tag_number: value}.
    exif = Image.open(path).getexif()

    # Screenshots and edited images often have no EXIF - say so cleanly.
    if not exif:
        print("No EXIF data found in this image.")
        return

    # Print each tag with its human-readable name.
    # TAGS.get(id, id) -> the friendly name, or the raw number if unknown.
    for tag_id, value in exif.items():
        print(f"{TAGS.get(tag_id, tag_id)}: {value}")


if __name__ == "__main__":
    # Try it on a photo straight off a phone (NOT a screenshot).
    show_exif("photo.jpg")
    # TODO (make it yours): add a "strip" mode that saves a clean copy
    # with the GPS/EXIF removed - that turns this into a privacy tool.
