#!/usr/bin/python
from PIL import Image
import os, sys

path = "/path/to/images"
dirs = os.listdir(path)
height = 100
width = 100
def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            print(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((width,height), Image.ANTIALIAS)
            imResize.save(f + '.jpg', 'JPEG', quality=90)

resize()