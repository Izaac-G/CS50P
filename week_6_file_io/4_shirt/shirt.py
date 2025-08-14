import sys, os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
        sys.exit("Extensions do not match")
    elif os.path.splitext(sys.argv[1])[1] != (".jpg" or ".jpeg" or ".png"):
        sys.exit("Invalid extension")
    else:
        fit_check(sys.argv[1], sys.argv[2])

def fit_check(input_file, output_file):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(input_file) as photo:
            photo = ImageOps.fit(photo, shirt.size)
            photo.paste(shirt, shirt)
            photo.save(output_file)
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
