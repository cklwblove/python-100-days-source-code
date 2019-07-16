# -*- coding: utf-8 -*-

from PIL import Image

image = Image.open('./ad_building.png')
image.format, image.size, image.mode
image.show()

for x in range(20):
    for y in range(33):
        z = 100 - x - y
        if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
            print(x, y, z)
