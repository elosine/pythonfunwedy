import math
import pyglet
from pyglet.gl import *

# STEP 1 - CREATE AN EQUATION SOLVING FUNCTION --------------------------- ##
## SOME BASIC PRINCIPLES (SKIP IF YOU ALREADY KNOW THESE)
#### BASIC FUNCTION
def basicFunctionExample(arg1, arg2):
    print (arg1*arg2)

print "Basic Function Example: "
basicFunctionExample(3, 5)

#### FUNCTION THAT RETURNS SOMETHING
def functionThatReturns(arg1, arg2):
    return arg1 * arg2

print "Function that returns: "
print functionThatReturns(99, 99)

#### FUNCTION THAT TAKES ANOTHER FUNCTION AS AN ARGUMENT ####
def argumentFunction (arg1, arg2):
    return arg1 - arg2

def mainFunction (func, arg3, arg4):
    return func(arg3, arg4) * arg3

print "Function that takes another function as an argument"
print mainFunction(argumentFunction, 7, 8)

## OK HERE WE GO
#### LET'S FIRST JUST MAKE A BASIC EQUATION Y = X3 (TO THE 3RD POWER)
def x3func(x):
    return math.pow(x,3)

print "x3 equation:"
print x3func(99)
#### NOW LET'S SOLVE IT FOR A RANGE OF VALUES
#### AND PLOP IT INTO AN ARRAY
#### AND RETURN THE ARRAY
def solveEquationForRangeFunction(equationFunc, range0, range1, numValues):
    # WE ARE GOING TO FEED THE EQUATION A NUMBER (NUMVALUES) OF 'X' VALUES
    # FROM RANGE0 TO RANGE1
    # HERE WE WILL FIND OUT HOW BIG THE RANGE IS (RANGE1-RANGE0)
    # AND THEN DIVIDE BY NUM VALUES TO GIVE THE SIZE OF EACH INCREMENT
    increment = (range1 - range0) / numValues
    # CREATE A LOOP THAT WILL SOLVE THE EQUATION FOR EVERY X IN THE RANGE
    vals = [] # empty (2d) array to store arrays of [x,y]
    currentVal = range0;
    while (currentVal <= range1):
        coords = [] # another empty array
        #store the x val (currentVal) in the coords array
        coords.append(currentVal)
        # equationFunc returns y value, add to coords array
        coords.append( equationFunc(currentVal) )
        # add these coords to the vals array
        vals.append(coords)
        #increment the currentVal
        currentVal = currentVal + increment
        #rinse, wash, repeat for numValues
    return vals

coordList = solveEquationForRangeFunction(x3func, 0.0, 1.0, 100.0)

print "Array of Coordinates:"
for x in coordList:
     print(x)

#STILL WITH ME?????
# coordList is a 2d array (and array of arrays) with the x and y Coordinates
# i.e. [ [0,1], [1,2], [2,3], [3,4] ... ]

## LET'S FINALIZE THE GRAPHING FUNCTION FROM ABOVE
def plotEquation(equationFunc, rangex0, rangex1, rangey0, rangey1, xwidth, yheight):
    vals = [];
    # The scaling is a factor of how many pixels each unit of the range equals
    # so if I have a window width of 1000, and my range is -4 to 4
    # the scale will be 1000/8 or 125
    # if I want to graph something at x = -3,
    # find out where it is in the range so simply -3 minus range0 or -4
    # so -3 - -4 = 1, and then 1 * the scaling or 125
    # so you plot at x=125px
    # this is confusing so we can talk it through
    widthScale = float(xwidth) / (rangex1 - rangex0)
    heightScale = float(yheight) / (rangey1 - rangey0)
    # loop through all the pixels in the x range
    for x in range(xwidth):
      xPlotVal = (x / widthScale) - rangex0
      yPlotVal = (equationFunc(xPlotVal) - rangey0) * heightScale
      xPlotVal = xPlotVal*widthScale
      # reverse y cause computer drawing system has 0 at top
      yPlotVal = yheight - yPlotVal
      #store in local array
      coords = [xPlotVal, yPlotVal];
      #push coords to vals array for later use
      vals.append(coords)
    return vals


winW = 600
winH = 600

graphData = plotEquation(x3func, 0.0, 1.0, 0.0, 1.0, winW, winH)
print graphData


#Lets Draw
## I'M SUGGESTING THAT YOU USE THE PYGLET LIBRARY
winCtrX = winW/2
winCtrY = winH/2
window = pyglet.window.Window(width=winW, height=winH)

# FUNCTION to draw a line
def drLine(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex2f(x1,y1) #pt1
    glVertex2f(x2,y2) #pt2
    glEnd()

# FUNCTION to plot graph data
def plotGraph(plotdata):
    for i, x in enumerate(plotdata):
        if i != 0:
            drLine(graphData[i-1][0], graphData[i-1][1], graphData[i][0], graphData[i][1])


# Create a Drawing Loop
@window.event
def on_draw():
    window.clear()
    # The whole GL context will take some getting used to but
    # Can do fancy graphics in the long run
    glLineWidth(3.0) #line thickness
    glColor3f(0.0,1.0,0.0) #line color (rgb 0.0-1.0)
    #Axes
    drLine(winCtrX, 0, winCtrX, winH)
    drLine(0, winCtrY, winW, winCtrY)

    #Draw Curve from points array
    glLineWidth(2.0) #line thickness
    glColor3f(1.0,1.0,0.0) #line color (rgb 0.0-1.0)
    plotGraph(graphData)

#Run pyglet App
pyglet.app.run()
