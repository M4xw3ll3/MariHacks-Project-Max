from PIL import Image, ImageChops
import base64
import math
import numpy as np

#converts 
file_name = "HelloWorld.mp3"
f = open(file_name ,'rb')
b = base64.b64decode(f.read())
x = ("".join(["{:08b}".format(x) for x in b]))
 
y = []
count = 0
for z in x:
    count += 1
    z = int(z)
    y.append(z)

size = round(math.sqrt(count))
img = Image.new('RGB', (size,size),"black")
pixels = img.load()

count2 =0
for i in range(size):
    for j in range(size):
        if y[count2] == 1:
            pixels[i,j] = (i, j, 255)
        elif y[count2] == 0:
            pixels[i,j] = (i, j, 000)
        count2 += 1
img.save("Pimage.png")
pixels2 = Image.open("redback.jpg")
w, h = pixels2.size
mod_img = img.resize((w, h))

n_image = np.array(mod_img)
n_red = np.array(pixels2)

im = Image.fromarray(np.uint8(n_image))
im2 = Image.fromarray(np.uint8(n_red))

n_new2 = ImageChops.add(im, im2, 1, 0)

im2.show()
im.show()
n_new2.show()
f.close()
