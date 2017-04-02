#Coordinates are being saved in hexadecimal digits
#The Adafruit led matrix uses rgb(7,7,7)
import os
import platform
import math
#from rgbmatrix import Adafruit_RGBmatrix

#Determine which platform is run to filepath conventions
myplatform = platform.system()

#Hex to RGB 255
def hextorgb(hex):
    #Return (red, green, blue) for the color given as #rrggbb.
    value = hex.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

#RGB(255,255,255) to RGB(7,7,7)
#NOT NECESSARY APPARENTLY
def matrixrgb(myrgb):
    myrgb = (myrgb/255)*7
    rgbdiv = math.ceil(myrgb)
    return rgbdiv

#Convert from letter to number
def converttoxy(coord):
	alphabetrows = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F']
	x, y = coord[:1], coord[1:]
	y = int(y) - 1
	x = alphabetrows.index(x)
	xycoords = (x,y)
	return xycoords

#Get full path name for files
def myfullfilepath(filename):
    global myplatform
    ext = ".txt"
    fullfilename = filename + ext
    print(myplatform)
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    if myplatform == 'Linux':
        rel_path = "pictures/" + fullfilename
    elif myplatform == 'Windows':
        rel_path = "pictures\\" + fullfilename
    abs_file_path = os.path.join(script_dir, rel_path)
    return abs_file_path

#Get user input to obtain filename
def getmyfilename():
    filename = input('Enter your desired filename: ')
    return filename

#Open file and read contents to matrix
def displaymyfilecoords():
    fromfile = ()
    rawname = getmyfilename()
    abs_file_path = myfullfilepath(rawname)
    file = open(abs_file_path, "r")
    for line in file:
        mysplit = line.split(',')
        for something in mysplit:
            colonsplit = something.split(':')
            if colonsplit[0] != '':
                xycoords = converttoxy(colonsplit[0])
                x = xycoords[0]
                y = xycoords[1]
                thiscolorrgb = hextorgb(colonsplit[1])
                r = matrixrgb(thiscolorrgb[0])
                g = matrixrgb(thiscolorrgb[1])
                b = matrixrgb(thiscolorrgb[2])
                #matrix.SetPixel(x,y,r,g,b)

displaymyfilecoords()
