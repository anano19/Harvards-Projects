import sys
from PIL import Image, ImageOps
import os

def main():
    if len(sys.argv) != 3:
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    input_extension = os.path.splitext(input_file)[1]
    output_extension = os.path.splitext(output_file)[1]
    if input_extension != output_extension:
        sys.exit(1)

    try:
        photo = Image.open(input_file)
        shirt = Image.open("shirt.png")
        crop= ImageOps.fit(photo, shirt.size)
        crop.paste(shirt, (0, 0), shirt)
        crop.save(output_file)
    except FileNotFoundError:
        sys.exit(1)


if __name__ == "__main__":
    main()
