import os
import sys

infile = sys.argv[1]

sect = os.path.splitext(infile)
ext = sect[1]
print(ext)