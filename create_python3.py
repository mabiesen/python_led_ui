#Purpose of this script is to control all UI interaction
from tkinter import *
from tkinter.colorchooser import *

import random
import re
import os
import platform

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

#Set our global variables
#colorcoords used to associate colors with coordinates
#coord comp used to associate tkinter.CURRENT integer with alphanumerical
#Note: the braces indicate empty dictionaries, not arrays
colorcoords = {}
coordcomp = {}
livepicturestorage = {}
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
            box = C.create_rectangle(x1,y1,x2,y2, fill="#000", outline="white", tags= thiscoord)
            C.tag_bind(box,'<Leave>',mouseover)
            colorcoords[thiscoord] = "#000"
            coordcomp[thiscoord] = x
            x = x + 1


#Paint brush event
def mouseover(event):
    if paintbrushon == True:
        if C.find_withtag(CURRENT):
            rect = C.find_withtag("current")[0]
            if rect < 1025:
                changeboxcolor(rect,currentcolor)

#These function calls kicks off program by creating grid and buttons for use
def startprogram():
    definesysvariables()
    creategrid()
    createbuttons()
    createbuttonlabels()

#kicks off the program by creating grid, buttons and labels
startprogram()

#Check for a click event
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
                changeboxcolor(x, "#000")
                x = x-1
        elif rect == 1027:
            x = 1024
            while x > 0:
                changeboxcolor(x, currentcolor)
                x = x-1
        elif rect ==1028:
            copyimagecoords()
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


#Continuing the click event checker...


#Change box color
def changeboxcolor(rect, color):
	global colorcoords
	coord = converttoletter(rect)
	C.itemconfig(rect, fill=color)
	colorcoords[coord] = color

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
        if color != "#000":
            f.write("%s:%s," % (coord,color))
    f.close
    print("File saved")

#Get full path name for files
def fullfilepath(filename):
    global myplatform
    ext = ".txt"
    fullfilename = filename + ext
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    if myplatform == 'Linux':
        rel_path = "pictures/" + fullfilename
    elif myplatform == 'Windows':
        rel_path = "pictures\\" + fullfilename
    abs_file_path = os.path.join(script_dir, rel_path)
    return abs_file_path

#Get user input to obtain filename
def getfilename():
    filename = input('Enter your desired filename: ')
    return filename

#Copy records to live storage
def copyimagecoords():
    global colorcoords
    global livepicturestorage
    livepicturestorage = {}
    print(len(livepicturestorage))
    for coord, color in colorcoords.items():
        if color != "#000":
            livepicturestorage[coord] = color

#Display picture from livestorage
def displayimage():
    global livepicturestorage
    print(len(livepicturestorage))
    for coord, color in livepicturestorage.items():
           coord = converttonumber(coord)
           changeboxcolor(coord,color)

#Convert from letter to number
def converttonumber(coord):
    global coordcomp
    print(coord)
    mynumber = coordcomp[coord]
    return mynumber

#Convert from number to letter
def converttoletter(coord):
    global coordcomp
    key=list(coordcomp.keys())[list(coordcomp.values()).index(coord)]
    return key

#Change the working color
def changecurrentcolor():
    global currentcolor
    selectedhex = getColor()
    currentcolor = selectedhex

def getColor():
    global currentcolor
    selectedcolor = askcolor()
    selectedhex = selectedcolor[1]
    if selectedhex is None:
        selectedhex = currentcolor
    return selectedhex



#Bind click event to canvas objects
C.bind("<Button-1>", click)

#Bind mouseover event to canvas objects
#C.bind( "<B1-Motion>", mouseover)

#End of Tkinter loop
root.mainloop(  )
