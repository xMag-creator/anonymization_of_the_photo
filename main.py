import sys
import os

try:
    from exif import Image
    print("exif module loaded")
except:
    print("No such module like exif")
    sys.exit(0)


def test_file(file: str) -> bool:
    """check if the file exists"""
    if not os.path.exists(file):
        return False
    return True


def open_image(file: str) -> Image:
    """Open the file"""
    with open(file, 'rb') as image_file:
        try:
            image = Image(image_file)
        except:
            return False

        return image


def info_exif(file_name: str):
    """reading and printing exif data"""
    if not test_file(file_name):
        print(f"No file: {file_name}")
        return None

    image_data = open_image(file_name)
    if not image_data:
        print("Wrong data")
        return None

    if not image_data.has_exif:
        print(f"No exif data for {file_name}")
        return None

    image_attribs = image_data.get_all()
    for attrib in image_attribs:
        value = image_attribs[attrib]
        print(f"Attribute: {attrib} = {value}")


def anonymize_exif(file_name: str):
    """Replacing original data"""
    pass


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        print(f"Started for one file: {args[1]} - information:")
        info_exif(args[1])
        sys.exit(0)
    else:
        print(f"Calling the script itself {args[0]} is impossible.")
        sys.exit(2)
