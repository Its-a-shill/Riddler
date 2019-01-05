from PIL import Image
import math
import os

#Creates the basic parts of the image
WIDTH = 100
HEIGHT = 100
image = Image.new('RGB', (WIDTH, HEIGHT))
imagePxls = list(image.getdata())


#Generates the map of bits
bits = [[False for i in range(HEIGHT)] for j in range(WIDTH)]
for y in range(1,HEIGHT):
    for x in range(1,WIDTH):
        if x >= y:
            bits[x][y] = not bits[x-y][y]
        else:
            bits[x][y] = not bits[x][y-x]

#Converts the map of bits into pixels (where blue is False and red is True)
for y in range(HEIGHT):
    for x in range(WIDTH):
        bit = 256 if bits[x][y] else 0
        imagePxls[(WIDTH-1-x)*HEIGHT+y] = (bit,0,256-bit)

image.putdata(imagePxls)
image.save("bits.png")
image.close()
