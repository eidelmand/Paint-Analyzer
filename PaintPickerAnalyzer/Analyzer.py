from PIL import Image
import io

deflist = [(250, 250, 250), (200, 200, 200), (150, 150, 150), (100, 100, 100), (50, 50, 50), (0, 0, 0)]
outlist = []
maxcolors = 15

def compareColor(rgb1, rgb2):
    out = abs(rgb1[0] - rgb2[0]) + abs(rgb1[1] - rgb2[1]) + abs(rgb1[2] - rgb2[2])
    return out



def compare(rgb, deflist):
    paint = deflist[0]
    dif = 10000
    for p in deflist:
        if compareColor(rgb,p) < dif:
            dif = compareColor(rgb,p)
            paint = p
    #print("closest to")
    outlist.append(p)
    #print(paint)

#this one is for dealing with a reference to image by path
def main(filename, numpaints, database):

    if numpaints >= 5 & numpaints <=35:
        maxcolors = numpaints
    if database!=None:
        deflist = database
    if filename != None:
        im = Image.open(filename)
    else:
        im = Image.open(filename)
    list = im.getcolors(im.size[0] * im.size[1])
    list.sort(reverse=True)
    j = 0

    while j < maxcolors:
        #print(list[j][0])
        #print(list[j][1])
        compare(list[j][1], deflist)
        j+= 1

    hold = outlist.copy()
    outlist.clear()
    #print(len(hold))
    return hold

#this one is for dealing with the image itself
def mainproper(file, numpaints, database):

    if numpaints >= 5 & numpaints <=35:
        maxcolors = numpaints
    if database!=None:
        deflist = database
    if file != None:
        im = Image.open(io.BytesIO(file))
    else:
        return
    list = im.getcolors(im.size[0] * im.size[1])
    list.sort(reverse=True)
    j = 0

    while j < maxcolors:
        print(list[j][0])
        print(list[j][1])
        compare(list[j][1], deflist)
        j+= 1

    hold = outlist.copy()
    outlist.clear()
    print(len(hold))
    return hold

#main("test.jpg",15,deflist)