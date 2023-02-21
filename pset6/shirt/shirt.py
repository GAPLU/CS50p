import sys
from PIL import Image
from PIL import ImageOps

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif sys.argv[1][-4:] != ".jpg" and sys.argv[1][-5:] != ".jpeg" and sys.argv[1][-4:] != ".png":
        sys.exit("Invalid input")
    elif sys.argv[2][-4:] != ".jpg" and sys.argv[1][-5:] != ".jpeg" and sys.argv[1][-4:] != ".png":
        sys.exit("Invalid output")
    elif sys.argv[1][-4:] != sys.argv[2][-4:]:
        sys.exit("Input and output have different extensions")

    try:
        file = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    image = ImageOps.fit(file, size=size)
    image.paste(shirt, shirt)
    image.save(sys.argv[2])


if __name__ == "__main__":
    main()