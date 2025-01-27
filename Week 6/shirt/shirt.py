import sys
import os
from PIL import Image
from PIL import ImageOps

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

infile = sys.argv[1]
outfile = sys.argv[2]

sect1 = os.path.splitext(infile)
ext1 = sect1[1]
# print(sect1[1])

sect2 = os.path.splitext(outfile)
ext2 = sect2[1]
# print(sect2[1])

extensions = [".png", ".jpeg", ".jpg"]

if not (ext1 in extensions):
    sys.exit("Invalid input")
if not (ext2 in extensions):
    sys.exit("Invalid output")
if ext1 != ext2:
    sys.exit("Input and output have different extensions")

try:
    open(infile)
except FileNotFoundError:
    sys.exit("Input does not exist")
else:
    shirt = Image.open("shirt.png")
    shirtSize = shirt.size
    print(shirtSize)

    fileShirt = Image.open(infile)
    imageSize = fileShirt.size
    print(imageSize)

    # print(type(imageSize[0]))
    # print(imageSize[0])
    # print(round(imageSize[0] / size[0]))

    resized_image = ImageOps.fit(fileShirt, (600, 600))
    sizeResized = resized_image.size
    print(sizeResized)

    resized_image.paste(shirt, shirt)
    resized_image.save(outfile)
    # factor = size[0] / imageSize[0]

    # ImageOps.scale(infile, size)
