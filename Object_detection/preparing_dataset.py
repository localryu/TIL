from PIL import Image
import os
import random
import string
from os.path import basename


def resizeImages(baseDir):
    basewidth = 558
    for filename in os.listdir(baseDir):
        filenameOnly, file_extension = os.path.splitext(filename)
        # print (file_extension)
        if (file_extension in [".jpg", '.png']):
            filepath = baseDir + os.sep + filename
            img = Image.open(filepath)
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize), Image.ANTIALIAS)
            img.save(filepath)
            print(filenameOnly, "Done")
    print('Done')


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def assignRandomNames(baseDir):
    for filename in os.listdir(baseDir):
        filepath = baseDir + os.sep + filename
        if os.path.isfile(filepath):
            finalFolder = baseDir
            filenameOnly, file_extension = os.path.splitext(finalFolder + os.sep + filename)
            os.rename(filepath, finalFolder + os.sep + id_generator() + file_extension)
            print(filenameOnly, "Done")

# Usage
baseDir = "/home/ryu/mbzirc/1/left/left/"	# change to the folder of the image
# resizeImages(baseDir)
assignRandomNames(baseDir)	# shuffle the name
