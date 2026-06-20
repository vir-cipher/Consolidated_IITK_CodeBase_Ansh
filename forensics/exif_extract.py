# exif_extract.py - see what a photo secretly remembers
# phones quietly stamp photos with the camera model, the time, and
# sometimes the EXACT gps spot. this reads that back. kinda scary tbh -
# post a holiday pic and you might be posting where you live too.
# spotting this is my first taste of "forensics".
#
# pip install pillow
from PIL import Image
from PIL.ExifTags import TAGS   # turns the numeric tag codes into names


def show_exif(path):
    exif = Image.open(path).getexif()      # gives {tag_number: value}

    # screenshots / edited images usually have no exif, say so cleanly
    if not exif:
        print("No EXIF data found in this image.")
        return

    for tag_id, value in exif.items():
        # TAGS.get(id, id) -> friendly name, or the raw number if unknown
        print(f"{TAGS.get(tag_id, tag_id)}: {value}")


if __name__ == "__main__":
    show_exif("photo.jpg")   # use a photo straight off a phone, NOT a screenshot
    # todo (make it mine): add a "strip" mode that saves a clean copy with
    # the gps/exif removed -> that turns this into an actual privacy tool.
