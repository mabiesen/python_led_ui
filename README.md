# Directions for Using the Python LED Program


**Soure code contributions to this project are welcomed!!!!!**

This project uses Python to provide a user interface for creating cool 32x32 LED Matrix displays.  The project can be used in concert with the matrix or alone as a sort of painting program.  Improvements forthcoming! Please be patient as this was my first dive into Python's Tkinter.

## Directions for Download

Please insure you have Python installed prior to downloading this program.  If you intend to use the Adafruit matrix, you will need to download Python 2 specifically (at this time, that comes standard in the Raspberry Pi Noobs download https://www.raspberrypi.org/downloads/noobs/).

#### UI portion of the project is functional at this time in Python 2 and 3.  To use:
1. download the zip of this Project using the green button at the top right side of the page.
2. extract to an isolated folder on your computer.
3. Run the file titled create_display.py

#### LED display portion of project is complete at this time on Python2.  To use:
1. download the zip of the project using the green button at the top right side of the page.
2. extract contents to an isolated folder on your computer
3. download the zip of the adafruit matrix library found at the following link https://github.com/adafruit/rpi-rgb-led-matrix
4. Extract the contents of this file to the folder that is housing the project
5. Per the directions at the link, under the "Running" section, you will need to create a make file for this matrix library.  This is really easy and only takes two lines of code in the terminal.
6. Make sure your LED display is hooked up (FRIENDLY REMINDER: MAKE SURE TH LED DISPLAY IS POWERED SEPARATELY FROM THE PI!!!)
7. Run the file titled create_display.py from the command line as a superuser
8. When prompted, type 'y' to allow for real time use with the LED Matrix.

*NOTE: At this time, you must refer to the Python shell(or your terminal) to save and retrieve stored file data*

*NOTE: When using the paintbrush feature, click and hold to stop painting.  This is counterintuitive and is on my todo list*

## Work To Be Done as of 4/5/2017

1. Change buttons to actual buttons.  Currently they are painted rectangles that act as buttons.
2. Provide a more program accessible way to request user information.  Currently the shell or terminal must be used to save or retrieve files, this is not very user friendly.  For retrieving files, provide a drop down selection.
3. I would prefer a live color wheel for color selection.  The current popup menu paradigm is not ideal.
4. Paintbrush feature should be fixed inverted.  Perhaps use mousedown detection to set a switch variable?
5. Currently, the code identifies Tkinter objects by their "indexed" tags.  This works but is sloppy coding from my perspective: potentially a change could be made to the program which affects the order in which our objects are created and thereby changes our indexed tags.  Using appropriate tags would also allow the code to be shortened as a conversion from "a1" format to indexed number would no longer be necessary.  Furthermore, doing this would afford the program an opportunity to change dimensions without concern in the event that someone has a 16x16 matrix.
6. Provide an area to show the current color.
7. Allow user to "turn off" led square by right clicking.
8. Better controls for window sizing.  Different Tkinter versions appear to affect the size of our matrix display.
9. Integrate image display for simple images.  This should be relatively easy using the Adafruit Library's existing code.
10. Integrate text display.  This would also be easy using the Adafruit Library's existing code.
11. Add to mabiesen.github.io. Maybe a video iframe of the tutorial.
12. ADD A TUTORIAL! It would be fun and provide added value:
* First integrate the text features from Adafruit's library
* Provide animated record functionality such that stored files can be displayed pixel-by-pixel to the matrix in the intended order, proviing the illusion of animation.
* Create folder to store tutorial data
* Create images and animations to display during the tutorial.
* Write the code to display changes in action
* Add a tutorial button

