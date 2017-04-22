import os
import sys

picturesdir = "pictures/"
#Get full path name for files
def fullfilepath(filename):
    ext = ".txt"
    fullfilename = filename + ext
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = picturesdir + fullfilename
    abs_file_path = os.path.join(script_dir, rel_path)
    return abs_file_path

#Get user input to obtain filename
def getfilename():
    if sys.version_info[:2] <= (2, 7):
        get_input = raw_input
    else:
        get_input = input
    filename = get_input('Enter your desired filename: ')
    return filename

#Hex to RGB 255
def hextorgb(hex):
    #Return (red, green, blue) for the color given as #rrggbb.
    value = hex.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

#Convert from letter to number
def converttoxy(coord):
	alphabetrows = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F']
	x, y = coord[:1], coord[1:]
	x = alphabetrows.index(x)
	xycoords = (x,y)
	return xycoords
