from PIL import Image
maxcolors = 15

def compareColor(rgb1, rgb2):
    out = abs(rgb1[0] - rgb2[0]) + abs(rgb1[1] - rgb2[1]) + abs(rgb1[2] - rgb2[2])
    return out

deflist = [(250,250,250), (200,200,200), (150,150,150), (100,100,100), (50,50,50), (0,0,0)]

def compare(rgb):
    paint = deflist[0]
    dif = 10000
    for p in deflist:
        if compareColor(rgb,p) < dif:
            dif = compareColor(rgb,p)
            paint = p
    print("closest to")
    print(paint)

im = Image.open('test.jpg')
list = im.getcolors(im.size[0] * im.size[1])
list.sort(reverse=True)
#print(list[0][0])
i = 0

#maxpix = im.getpixel((0,0))
#maxnum = 0
j = 0

while j < maxcolors:
    print(list[j][0])
    print(list[j][1])
    compare(list[j][1])

    j+= 1
#    if len(list) > 0:
 #       while i < len(list):
  #          if list[i][0] > maxnum:
   #             maxnum = list[i][0]
    #            maxpix = list[i][1]
     #       i+= 1

#print(maxpix)