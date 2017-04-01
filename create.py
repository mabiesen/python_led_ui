
#Purpose of this script is to control all UI interaction
from tkinter import *
import random
import re
import os

#Set our global variables
#colorcoords used to associate colors with coordinates
#coord comp used to associate tkinter.CURRENT integer with alphanumerical
#Note: the braces indicate empty dictionaries, not arrays
colorcoords = {}
coordcomp = {}
livepicturestorage = {}
fromfile = {}
currentcolor = "blue"

#Initialize tkinter
root = Tk(  )

C = Canvas(root, bg="blue", height=1400, width=2400)

C.pack()

#Create the grid.  Simultaneously add to output array
def creategrid():
    global colorcoords
    global coordcomp
    alphabetrows = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F']
    x = 1
    for r in range(32):
        letter = alphabetrows[r]
        for c in range(32):
            x1 = 10 + (c*40)
            y1 = 10 + (r*40)
            x2 = x1 + 40
            y2 = y1 + 40
            C.create_rectangle(x1,y1,x2,y2, fill="black", outline="white")
            thiscoord = letter + str(c+1)
            colorcoords[thiscoord] = "black"
            coordcomp[thiscoord] = x
            x = x + 1

#This function call kicks off program by creating grid for use
creategrid()

#Check for a click event
#Handles all click events
def click(event):
    global colorcoords
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
                changeboxcolor(x, "black")
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


#Continuing the click event checker...


#Change box color
def changeboxcolor(rect, color):
	global colorcoords
	coord = converttoletter(rect)
	C.itemconfig(rect, fill=color)
	colorcoords[coord] = color

#use file coordinates to populate pictures on screen
def getfilecoords():
    fromfile = {}
    rawname = getfilename()
    abs_file_path = fullfilepath(rawname)
    file = open(abs_file_path, "r")
    for line in file:       
        mysplit = line.split(',')
        for something in mysplit:
            colonsplit = something.split(':')
            coord = converttonumber(colonsplit[0])
            changeboxcolor(coord,colonsplit[1])
            


#print coordinates to file located in python project subdirectory
def printcoords(filename):
    global colorcoords
    abs_file_path = fullfilepath(filename)
    f = open(abs_file_path,"w+")
    for coord, color in colorcoords.items():
        if color != "black":
            f.write("%s:%s," % (coord,color))
    f.close
    print("File saved")

#Get full path name for files
def fullfilepath(filename):
	ext = ".txt"
	fullfilename = filename + ext
	script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
	rel_path = "pictures/" + fullfilename
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
        if color != "black":
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
    color = ["red", "orange", "yellow", "green", "blue", "violet"]
    currentcolor = random.choice(color)


#rectangle to change the current color
# reference tag 1025
C.create_rectangle(1650,50,1800,150, fill="yellow")

#rectangle to fill black
# reference tag 1026
C.create_rectangle(1650,200,1800,300, fill="orange")

#rectangle to fill current color
# reference tag 1027
C.create_rectangle(1650,350,1800,450, fill="red")

#rectangle to collect non-black coordinates and store for live use
# reference tag 1028
C.create_rectangle(1650,500,1800,600, fill="violet")

#rectangle to show live coordinates
# reference tag 1029
C.create_rectangle(1650,650,1800,750, fill="black")

#rectangle to print to file in project subdirectory
# reference tag 1030
C.create_rectangle(1650,800,1800,900, fill="green")

#Recall contents from file and display on screen
# reference tag 1031
C.create_rectangle(1650,950,1800,1050, fill="brown")

#Bind click event to canvas objects
C.bind("<Button-1>", click)

#End of Tkinter loop
root.mainloop(  )