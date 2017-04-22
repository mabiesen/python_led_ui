import util

myfilename = util.getfilename()
print("Filename provided by user is\n %s" % myfilename)

myfilepath = util.fullfilepath(myfilename)
print("The filepath for the provided file is\n %s" % myfilepath)

myhex = "#ffffff"
t = util.hextorgb(myhex)
print("The equivalent rgb values for #ffffff are \n %d,%d,%d" %(t[0], t[1], t[2]))

mycoord = "b3"
coordtuple = util.converttoxy(mycoord)
print("For coordinate b3, x coordinate is %s, and the y coordinate is %s" %(coordtuple[0], coordtuple[1]))
