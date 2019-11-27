from graphics import * #a library that allows me to draw lines, shapes and characters

win = GraphWin('visual calculus', 690, 690) #creates a window in which graphics can be drawn
width = win.getWidth() # save the width and height of the window
height = win.getHeight()
midpointX = width/2 #get the midpoints of the window(width and height)
midpointY = height/2
edgeGap = height/25 #set a reasonable space between the ends of the axes and thre edge of the window( 1/25th of the height)
incrementX = (width-2*edgeGap)/20 # set the space between each increment on the axes
incrementY = (height-2*edgeGap)/20
XAxis = Line(Point(midpointX,edgeGap),Point(midpointX,height-edgeGap)) # create the axes
YAxis = Line(Point(edgeGap,midpointY),Point(width-edgeGap,midpointY))
XAxis.draw(win) #draw the axes
YAxis.draw(win)
for i in range(0,21): #draw 20 small, equally spaced lines on each axis to see increments
    incrementLineX = Line(Point(edgeGap+(i*incrementX),midpointY),Point(edgeGap+(i*incrementX),midpointY+7))
    incrementLineY = Line(Point(midpointX-7,edgeGap+(i*incrementY)),Point(midpointX, edgeGap+(i*incrementY)))
    incrementLineX.draw(win)
    incrementLineY.draw(win)

for j in range(0,10): #draw the numbers -10 to -1 at each line (left to right) on the x axis and 10 to 1 at each line(top to bottom) on the y axis
    numX = Text(Point(edgeGap+(j*incrementX)-2,midpointY+12),str(j-10))
    numY = Text(Point(midpointX-15,edgeGap+(j*incrementY)),str(-(j-10)))
    numX.setSize(8)
    numY.setSize(8)
    numX.draw(win)
    numY.draw(win)

for k in range(11,21): #draw the numbers 1 to 10 on the other side of the x axis and the numbers -1 to -10 on the othe side of the y axis
    numX = Text(Point(edgeGap+(k*incrementX),midpointY+12),str(k-10))
    numY = Text(Point(midpointX-15,edgeGap+(k*incrementY)),str(-(k-10)))
    numX.setSize(8)
    numY.setSize(8)
    numX.draw(win)
    numY.draw(win)


x3 = 2
x2 = 1
x = 4
c = 2
points = []
for i in range (0,2000):
    xGraphValue = (i/100)-10
    yGraphValue = x3*xGraphValue**3 + x2*xGraphValue**2 + x*xGraphValue + c
    xPixelValue = midpointX + xGraphValue*incrementX
    yPixelValue = 690-(midpointY + yGraphValue*incrementY)
    points.append(Point(xPixelValue,yPixelValue))


for i in range(0,1999):
    joinLine = Line(points[i],points[i+1])
    joinLine.draw(win)
