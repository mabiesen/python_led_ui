# python_led_ui
Project to use python as a user interface for creating cool 32x32 LED Matrix displays

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

Project issue: Python 3 is not compatible with Adafruit matrix library
Project issue: Python 2 and Python 3 have different input and import statements

My solution to these dilemmas is to use try and except statements to pull in libraries with the compatible import statements, allowing the UI environment to run on both python 2 and 3.  I also have an if statement that checks for the user's python version before attempting to access the Adafruit matrix library.
