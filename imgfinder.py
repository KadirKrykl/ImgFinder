import numpy
from PIL import Image

smallIMG = input("Enter path of the small img:")
bigIMG = input("Enter path of the big img:")

small = Image.open(smallIMG)
big  = Image.open(bigIMG)
bigar  = numpy.asarray(big)
bigary,  bigarx  = bigar.shape[:2]

finded = False

for i in range(4):
    small = small.rotate(90)
    smaller  = numpy.asarray(small)
    smallery, smallerx = smaller.shape[:2]
    stopx = bigarx - smallerx + 1
    stopy = bigary - smallery + 1

    for x in range(0, stopx):
        for y in range(0, stopy):
            x2 = x + smallerx
            y2 = y + smallery
            pic = bigar[y:y2, x:x2]
            test = (pic == smaller)
            if test.all():
                w, h = small.size
                print("Left-Top:{0},{1}".format(x,y))
                print("Right-Top:{0},{1}".format(x+w,y))
                print("Left-Bottom:{0},{1}".format(x,y-h))
                print("Right-Bottom:{0},{1}".format(x+w,y-h))
                finded = True
                break
        if finded:
            break
    if finded:
            break

