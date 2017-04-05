# Directions for Using the Python LED Program


This project uses Python to provide a user interface for creating cool 32x32 LED Matrix displays.  The project can be used in concert with the matrix or alone as a sort of painting program.

## Directions for Download

UI portion of the project is functional at this time in Python3.  To use:
1. download the zip of this Project
2. extract to an isolated folder
3. Run the file titled create_display.py

LED display portion of project is complete at this time on Python2.  To use:
1. download the zip of the project
2. extract contents to an isolated folder
3. download the zip of the adafruit matrix library found at the following link https://github.com/adafruit/rpi-rgb-led-matrix
4. Extract the contents of this file to the folder that is housing the project
5. Per the directions at the link, under the "Running" section, you will need to create a make file for this matrix library.
6. Make sure your LED display is hooked up (FRIENDLY REMINDER: MAKE SURE TH LED DISPLAY IS POWERED SEPARATELY FROM THE PI!!!)
7. Run the file titled create_display.py from the command line as a superuser
8. When prompted, type 'y' to allow for real time use with the LED Matrix.

*NOTE: At this time, you must refer to the Python shell(or your terminal) to save and retrieve stored file data*

*NOTE: When using the paintbrush feature, click and hold to stop painting.  This is counterintuitive and is on my todo list*

## Work To Be Done

1. Change buttons to actual buttons.  Currently they are painted rectangles that act as buttons.
2. Provide a more program accessible way to request user information.  Currently the shell or terminal must be used to save or retrieve files, this is not very user friendly.  For retrieving files, provide a drop down selection.
3. I would prefer a live color wheel for color selection.  The current popup menu paradigm is not ideal.
4. Paintbrush feature should be fixed inverted.  Perhaps use mousedown detection to set a switch variable?
5. Currently, the code identifies Tkinter objects by their "indexed" tags.  This works but is sloppy coding from my perspective: potentially a change could be made to the program which affects the order in which our objects are created and thereby changes our indexed tags.  Using appropriate tags would also allow the code to be shortened as a conversion from "a1" format to indexed number would no longer be necessary.

