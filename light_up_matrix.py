#Coordinates are being saved in hexadecimal digits
#The Adafruit led matrix uses rgb(7,7,7)

#from rgbmatrix import Adafruit_RGBmatrix

#Hex to RGB 255
def hextorgb(hex):
    #Return (red, green, blue) for the color given as #rrggbb.
    value = hex.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

#RGB(255,255,255) to RGB(7,7,7)
def matrixrgb(myrgb):
    x = 0
    while x < len(myrgb):
	rgbmod = myrgb[x]%7
	rgbdiv = myrgb/7 - rgbmod
	myrgb[x] = rgbdiv
	x = x + 1
    return myrgb

#Display coords on led matrix
def lightupmatrix(xcoord,ycoord,myrgb):
	red = myrgb[0]
	green = myrgb[1]
	blue = myrgb[2]
	matrix.SetPixel(xcoord,ycoord,red,green,blue)
	#matrix.SetPixel() vs matrix.drawPixel()?

mytuple = hextorgb('#ffffff')
print(mytuple)
