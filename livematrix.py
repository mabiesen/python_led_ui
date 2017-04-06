from rgbmatrix import Adafruit_RGBmatrix

def livereading(coord, color):
	xycoords = util.converttoxy(coord)
	x = int(xycoords[0])
	y = int(xycoords[1])
	#error in x coord? backwards, correcting
	if y > 16:
		y = 16-(y-16)
	else:
		y = 16 + (16-y)


	thiscolorrgb = util.hextorgb(color)
	r = int(thiscolorrgb[0])
	g = int(thiscolorrgb[1])
	b = int(thiscolorrgb[2])
	matrix.SetPixel(x,y,r,g,b)
