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

import util
import platform

livedisplay = False

#Determine if user has active LED display
if sys.version_info[:2] <= (2, 7):
	uinput = raw_input("You have the requirements necessary to work with an LED display.  Would you like to use the LED display in real time?(y/n)")
	if uinput == "y":
		print("You selected yes.  Sounds great! The matrix library will be loaded")
		livedisplay = True
		import livematrix
		matrix = Adafruit_RGBmatrix(32,1)
	else:
		print("The matrix will not be utilized")
else:
	print("You do not have the necessary requirements for a live LED matrix.")
#Determine which platform is run to filepath conventions
myplatform = platform.system()

#Set sysvariables globally
#THESE VALUES MEAN NOTHING, this is being done to insure variables global
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
    global picturesdir
    if myplatform == "Windows":
        buttonstartx = 700
        buttonendx = 800
        buttonstarty = 10
        buttonyheight = 40
        buttonspace = 50
        matrixspace = 20
        picturesdir = "pictures\\"
    if myplatform == "Linux":
        buttonstartx = 1300
        buttonendx = 1400
        buttonstarty = 10
        buttonyheight = 40
        buttonspace = 50
        matrixspace = 40
        picturesdir = "pictures/"
    return (buttonstartx, buttonendx, buttonstarty, buttonyheight, buttonspace, matrixspace)

#MIDDLECLICK EVENT
#Used to set paintburshon variable
def middleclick(event):
	global paintbrushon
	if paintbrushon == True:
		paintbrushon = False
	else:
		paintbrushon = True

#BOX ON ENTER EVENT
def mouseover(event):
    if paintbrushon == True:
        if C.find_withtag(CURRENT):
            rect = C.find_withtag("current")[0]
            if rect < 1025:
                changeboxcolor(rect,currentcolor)

#CLICK EVENTS FOR MATRIX BOXES
def leftclick(event):
    global colorcoords
    if C.find_withtag(CURRENT):
        rect = C.find_withtag("current")[0]
        if rect < 1025:
            changeboxcolor(rect,currentcolor)
            C.update_idletasks()

def rightclick(event):
    global colorcoords
    if C.find_withtag(CURRENT):
        rect = C.find_withtag("current")[0]
        if rect < 1025:
            changeboxcolor(rect,"#000000")
            C.update_idletasks()

#BUTTON CLICK EVENTS
def buttonclick(button):
    global paintbrushon
    if button == 0:
        changecurrentcolor()
    elif button == 1:
        x = 1024
        while x > 0:
            changeboxcolor(x, "#000000")
            x = x-1
    elif button == 2:
        x = 1024
        while x > 0:
            changeboxcolor(x, currentcolor)
            x = x-1
    elif button == 3:
        copytempcoords()
    elif button == 4:
        displayimage()
    elif button == 5:
        filename = util.getfilename()
        printcoords(filename)
    elif button == 6:
        filename = util.getfilename()
        getfilecoords(filename)

#Create buttons that will be used in the game
#Buttons immediately created after grid and assigned index values 1025 through number of buttons
def createbuttons(buttonstartx, buttonendx, buttonstarty, buttonyheight, buttonspace):
    mybuttontags = ("colorselection", "fillblack", "fillcolor", "tempsave", "tempdisplay", "savefile", "displayfile")
    mylabels = ("Select a Color","Fill Matrix Black","Fill Matrix Color","Temp Save","Temp Display","Save To File", "Pull From File")
    x=0
    while x < 7:
        buttoncurrenty = buttonstarty + (x * buttonspace)
        #C.create_rectangle(buttonstartx,buttoncurrenty,buttonendx, buttoncurrenty + buttonyheight, fill=buttoncolor[x], tags=mybuttontags[x])
        b = Button(root, text=mylabels[x], command=lambda j=x: buttonclick(j), font=("Helvetica",14))
        b.pack()
        b.place(x=buttonstartx, y=buttoncurrenty, height=buttonyheight)
        x = x + 1

def createcurrentcolorbox(buttonstartx, buttonstarty, buttonendx, buttonyheight):
    C.create_rectangle(buttonstartx + 400, buttonstarty, buttonendx + 400, buttonstarty + buttonyheight, fill=currentcolor)

#Create the grid.  Simultaneously add to output array
#Create grid is called first to insure that box object have the correct indices
def creategrid(matrixspace):
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
    lov = definesysvariables()
    creategrid(lov[5])
    createcurrentcolorbox(lov[0], lov[2], lov[1], lov[3])
    createbuttons(lov[0], lov[1], lov[2], lov[3], lov[4])
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
#If user has opted for live display, displays to LED matrix using livematrix.py
def changeboxcolor(rect, color):
	global colorcoords
	coord = converttoletter(rect)
	C.itemconfig(rect, fill=color)
	colorcoords[coord] = color
	if livedisplay == True:
		livematrix.livereading(coord, color)

#use file coordinates to populate pictures on screen
def getfilecoords(rawname):
    abs_file_path = util.fullfilepath(rawname)
    file = open(abs_file_path, "r")
    for line in file:
        mysplit = line.split(',')
        for something in mysplit:
            colonsplit = something.split(':')
            if colonsplit[0] != '':
                coord = converttonumber(colonsplit[0])
                changeboxcolor(coord,colonsplit[1])

#write coordinates to file located in python project subdirectory
def printcoords(filename):
    global colorcoords
    abs_file_path = util.fullfilepath(filename)
    f = open(abs_file_path,"w+")
    for coord, color in colorcoords.items():
        if color != "#000000":
            f.write("%s:%s," % (coord,color))
    f.close
    print("File saved")

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
    C.itemconfig(1025, fill=currentcolor)

#Color selection from Tkinter colorchooser module
def getColor():
    global currentcolor
    selectedcolor = askcolor()
    selectedhex = selectedcolor[1]
    if selectedhex is None:
        selectedhex = currentcolor
    return selectedhex

#Bind click event to all canvas objects
C.bind("<Button-1>", leftclick)
C.bind("<Button-2>", middleclick)
C.bind("<Button-3>", rightclick)

#End of Tkinter loop
root.mainloop()
