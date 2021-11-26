from PIL import Image
import math
import sys
import os

# character mapping options
#chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
#chars = "$Xx=+;:. "
chars = "$=:."

# ensuring proper args included
path = None;
if len(sys.argv) == 1:
    path = input("Image path:")
elif len(sys.argv) == 2:
    path = sys.argv[1]
else:
    print("ERROR maximum of one argument")
    sys.exit()
    
# open image
try:
    im = Image.open(path, 'r')
    width, height = im.size
    pixel_values = list(im.getdata())
except:
    print("ERROR cannot open image")
    sys.exit()

# set output file path and name
output = path
char = output[-1]
while char != ".":
    output = output[:-1]
    char = output[-1]
output = output[:-1]
output += "_to_text.txt"

# open/create output file and clear it
f = open(output, "a")
f.truncate(0)

# get avg brightness of every pixel and map it to text char
for y in range(height):
    for x in range(width): 
        r,g,b = pixel_values[width*y+x]
        brightness = (r+g+b)/3
        brightPerc = brightness/255
        charIndex = math.floor(brightPerc * len(chars) - 1)
        f.write(chars[charIndex] + " ")
        if x == width - 1: 
            f.write("\n")

f.close()

print("Successfully created", output)
