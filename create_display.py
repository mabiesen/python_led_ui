#Purpose of this script is to control all UI interaction
#This script is written in Python 2 form to cater to RPI LED matrix library

#Python3 - from tkinter import *
#Python2 - from Tkinter import *
try:
    from tkinter import *
except ImportError:
    from Tkinter import *

#Python3 - from tkinter.colorchooser import *
#Python2 - from tkColorChooser import *
try:
    from tkinter.colorchooser import *
except ImportError:
    from tkColorChooser import *

import os
import platform

livedisplay = False

#Determine if user has active LED display
if sys.version_info[:2] <= (2, 7):
	uinput = raw_input("You have the requirements necessary to work with an LED display.  Would you like to use the LED display in real time?(y/n)")
	if uinput == "y":
		print("You selected yes.  Sounds great! The matrix library will be loaded")
		livedisplay = True
		#from rgbmatrix import Adafruit_RGBmatrix
		matrix = Adafruit_RGBmatrix(32,1)
	else:
		print("The matrix will not be utilized")
else:
	print("You do not have the necessary requirements for a live LED matrix.")
#Determine which platform is run to filepath conventions
myplatform = platform.system()

#Set sysvariables globally
#THESE VALUES MEAN NOTHING, this is being done to insure variables global
buttonstartx = 1300
buttonendx = 1400
buttonstarty = 10
buttonyheight = 40
buttonspace = 50
labelstartx = 900
labelstarty = 30
labelspace = 50
matrixspace = 40
picturesdir = "pictures/"

#Set our global variables that are not system dependent
#colorcoords used to associate colors with coordinates
#coord comp used to associate tkinter.CURRENT integer tag with alphanumerical
#temppicturestorage is for the tempdisplay module
#currentcolor holds starting color until user selects a new color
#paintbrushon variable used as a toggle switch for paintbrush functionality
#Note: the braces indicate empty dictionaries, not arrays
colorcoords = {}
coordcomp = {}
temppicturestorage = {}
currentcolor = "#5595AB"
paintbrushon = False

#Initialize tkinter
root = Tk(  )
root.title("User Interface for 32 x 32 LED Display")
C = Canvas(root, bg="white", height=1400, width=2400)
C.pack()

#define some system dependent variables
def definesysvariables():
    global buttonstartx
    global buttonendx
    global buttonstarty
    global buttonyheight
    global buttonspace
    global labelstartx
    global labelstarty
    global labelspace
    global matrixspace
    global picturesdir
    if myplatform == "Windows":
        buttonstartx = 700
        buttonendx = 800
        buttonstarty = 10
        buttonyheight = 40
        buttonspace = 50
        labelstartx = 900
        labelstarty = 30
        labelspace = 50
        matrixspace = 20
        picturesdir = "pictures\\"
    if myplatform == "Linux":
        buttonstartx = 1300
        buttonendx = 1400
        buttonstarty = 10
        buttonyheight = 40
        buttonspace = 50
        labelstartx = 1580
        labelstarty = 30
        labelspace = 50
        matrixspace = 40
        picturesdir = "pictures/"

#BOX ON ENTER EVENT
def mouseover(event):
    if paintbrushon == True:
        if C.find_withtag(CURRENT):
            rect = C.find_withtag("current")[0]
            if rect < 1025:
                changeboxcolor(rect,currentcolor)

#CLICK EVENTS
#Handles all click events
def click(event):
    global colorcoords
    global paintbrushon
    if C.find_withtag(CURRENT):
        rect = C.find_withtag("current")[0]
        if rect < 1025:
            changeboxcolor(rect,currentcolor)
            C.update_idletasks()
        elif rect == 1025:
            changecurrentcolor()
        elif rect == 1026:
            x = 1024
            while x > 0:
                changeboxcolor(x, "#000000")
                x = x-1
        elif rect == 1027:
            x = 1024
            while x > 0:
                changeboxcolor(x, currentcolor)
                x = x-1
        elif rect ==1028:
            copytempcoords()
        elif rect == 1029:
            displayimage()
        elif rect == 1030:
            filename = getfilename()
            printcoords(filename)
        elif rect == 1031:
            getfilecoords()
        elif rect == 1032:
            if paintbrushon == False:
                paintbrushon = True
            else:
                paintbrushon = False

#Create buttons that will be used in the game
#Buttons immediately created after grid and assigned index values 1025 through number of buttons
def createbuttons():
    buttoncolor = ("yellow","orange","red","violet","black","green","brown","blue")
    x=0
    while x < 8:
        buttoncurrenty = buttonstarty + (x * buttonspace)
        C.create_rectangle(buttonstartx,buttoncurrenty,buttonendx, buttoncurrenty + buttonyheight, fill=buttoncolor[x])
        x = x + 1

#Create labesls that will be used for our buttons
#Labels placed to side of buttton to avoid object index clash when button is clicked
#Labels are created after buttons to insure that buttons are assigned the correct index
def createbuttonlabels():
    mylabels = ("Select a Color","Fill Matrix Black","Fill Matrix Color","Temp Save","Temp Display","Save To File", "Pull From File", "Paintbrush")
    x = 0
    while x < 8:
        C.create_text(labelstartx,labelstarty + (x * labelspace), text=mylabels[x], font=("Helvetica",14))
        x = x + 1

#Create the grid.  Simultaneously add to output array
#Create grid is called first to insure that box object have the correct indices
def creategrid():
    global colorcoords
    global coordcomp
    alphabetrows = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F']
    x = 1
    for r in range(32):
        letter = alphabetrows[r]
        for c in range(32):
            x1 = 10 + (c*matrixspace)
            y1 = 10 + (r*matrixspace)
            x2 = x1 + matrixspace
            y2 = y1 + matrixspace
            thiscoord = letter + str(c+1)
            box = C.create_rectangle(x1,y1,x2,y2, fill="#000000", outline="white", tags= thiscoord)
            C.tag_bind(box,'<Enter>',mouseover)
            colorcoords[thiscoord] = "#000000"
            coordcomp[thiscoord] = x
            x = x + 1

#START PROGRAM
#These function calls kicks off program by creating grid and buttons for use
#I placed these calls down here, after the program has read the functions that are being called
def startprogram():
    definesysvariables()
    creategrid()
    createbuttons()
    createbuttonlabels()
#kicks off the program by creating grid, buttons and labels
startprogram()

#...............................
# All functions above this line helped to set up the program
# Mouseover and click events placed at top since referenced in setup
# C offers prototyping for this issue, not certain if Python does
#
#All functions below this line are related to in-program events
#...............................


#Change box color.  Paints the box a new color
#If user has opted for live display, displays to LED matrix
def changeboxcolor(rect, color):
	global colorcoords
	coord = converttoletter(rect)
	C.itemconfig(rect, fill=color)
	colorcoords[coord] = color
	if livedisplay == True:
		livereading(coord, color)


#use file coordinates to populate pictures on screen
def getfilecoords():
    rawname = getfilename()
    abs_file_path = fullfilepath(rawname)
    file = open(abs_file_path, "r")
    for line in file:
        mysplit = line.split(',')
        for something in mysplit:
            colonsplit = something.split(':')
            if colonsplit[0] != '':
                coord = converttonumber(colonsplit[0])
                changeboxcolor(coord,colonsplit[1])


#print coordinates to file located in python project subdirectory
def printcoords(filename):
    global colorcoords
    abs_file_path = fullfilepath(filename)
    f = open(abs_file_path,"w+")
    for coord, color in colorcoords.items():
        if color != "#000000":
            f.write("%s:%s," % (coord,color))
    f.close
    print("File saved")

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

#Copy records to live storage
def copytempcoords():
    global colorcoords
    global temppicturestorage
    temppicturestorage = {}
    for coord, color in colorcoords.items():
        if color != "#000000":
            temppicturestorage[coord] = color

#Display picture from livestorage
def displayimage():
    global temppicturestorage
    for coord, color in temppicturestorage.items():
           coord = converttonumber(coord)
           changeboxcolor(coord,color)

#Convert coordinates from letter to number
def converttonumber(coord):
    global coordcomp
    mynumber = coordcomp[coord]
    return mynumber

#Convert coordinates from number to letter
def converttoletter(coord):
    global coordcomp
    key=list(coordcomp.keys())[list(coordcomp.values()).index(coord)]
    return key

#Change the working color
def changecurrentcolor():
    global currentcolor
    selectedhex = getColor()
    currentcolor = selectedhex

#Color selection from Tkinter colorchooser module
def getColor():
    global currentcolor
    selectedcolor = askcolor()
    selectedhex = selectedcolor[1]
    if selectedhex is None:
        selectedhex = currentcolor
    return selectedhex

#.........................
#This next section is for livedisplay only
#.........................

#LIVE WORK WITH LED MATRIX DISPLAY
#Notes are generalized function are generalized
#Read all coordinates live from create.py
#Prior to the live reading, coordinates must be submitted individually
#Coordinates will need to be converted before use
#On close I will need to clear the matrix screen

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
	y = int(y) - 1
	x = alphabetrows.index(x)
	xycoords = (x,y)
	return xycoords

def livereading(coord, color):
	xycoords = converttoxy(coord)
	x = int(xycoords[0])
	#error in x coord? backwards, correcting
	if x > 16:
		x = 16-(x-16)
	else:
		x = 16 + (16-x)

	y = int(xycoords[1])
	thiscolorrgb = hextorgb(colonsplit[1])
	r = int(matrixrgb(thiscolorrgb[0]))
	g = int(matrixrgb(thiscolorrgb[1]))
	b = int(matrixrgb(thiscolorrgb[2]))
	#matrix.SetPixel(x,y,r,g,b)



#Bind click event to all canvas objects
C.bind("<Button-1>", click)


#End of Tkinter loop
root.mainloop(  )
