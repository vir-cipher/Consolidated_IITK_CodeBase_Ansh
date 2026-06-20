"""
exif_extract.py - see what a photo secretly remembers.

phones quietly stamp photos with metadata (EXIF): the camera model, the exact
date/time, and sometimes the GPS coordinates where it was taken. this reads
that back out. kinda scary tbh - post a holiday pic straight off your phone
and you might be posting your home address too. spotting this is my first
taste of "forensics": the evidence is sitting inside the file, you just have
to know to look.

what youll usually see: Make, Model, DateTime, and (the spicy one) GPSInfo.
screenshots and chat-app images normally have it all stripped, so dont be
surprised when those come back empty.

needs Pillow:  pip install pillow
"""
from PIL import Image
from PIL.ExifTags import TAGS   # turns the numeric tag codes into names


def show_exif(path):
    """Print every EXIF tag in the image at `path` as `Name: value`.

    Args:
        path: a photo straight off a camera/phone (NOT a screenshot).
    Example:
        >>> show_exif("photo.jpg")
        Make: Apple
        Model: iPhone 12
        DateTime: 2024:01:05 14:22:10
        GPSInfo: {...}
    """
    exif = Image.open(path).getexif()      # -> {tag_number: value}

    # screenshots / edited images usually have no exif - say so cleanly
    # instead of printing nothing and looking broken.
    if not exif:
        print("No EXIF data found (probably a screenshot, or it was stripped).")
        return

    for tag_id, value in exif.items():
        # TAGS.get(id, id) -> friendly name like "Model", or the raw number
        # if its a tag Pillow doesnt recognise.
        name = TAGS.get(tag_id, tag_id)
        print(f"{name}: {value}")
        if name == "GPSInfo":
            print("   ^ this can pin the photo to an exact spot on a map.")


if __name__ == "__main__":
    show_exif("photo.jpg")   # use a photo straight off a phone, NOT a screenshot
    # todo (make it mine): add a "strip" mode that saves a clean copy with the
    # gps/exif removed -> that turns this from a viewer into a privacy tool.
