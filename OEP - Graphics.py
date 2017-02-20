# Tyler Collins and James Gelok
# OEP.py
from graphics import *
import math

def main():
    global image
    global bike
    global direction
    global image
    
    filename = "Black-window.png"
    image = Image(Point(100, 100), filename)
    size = image.getWidth()
    
    window = GraphWin("Tron", size , size)
    window.setCoords(0, 0, 200, 200)

    image.draw(window)

    bike = Circle(Point(100, 100), 3)
    bike.setFill('goldenrod')
    bike.draw(window)

    move()

def getCoords(shape):
    x = int(shape.p2.x - (abs(shape.p1.x - shape.p2.x) / 2))
    y = int(shape.p2.y - (abs(shape.p1.y - shape.p2.y) / 2))
    print(x,y)
    return x, y
    
def move():
    global bike
    global moving
    global image
    
    moving = True
    
    while moving:
        moveCircle(bike)
        x,y = getCoords(bike)
        colorChk(x, y)
def moveCircle(shape):
    global direction
            #add if statments here
    stupid = input("Direction:")
    if stupid == "w":
        bike.move(0, 2) #up
    elif stupid == "s":
        bike.move(0, -2)#down
    elif stupid == "a":
        bike.move(-2, 0)#left
    elif stupid == "d":
        bike.move(2, 0)#right
        
def colorChk(x,y):
    global moving
    global image
    
    pixel = image.getPixel(x, y)
    print(pixel)
    if pixel == [0, 0, 0]:
        image.setPixel(x, y, "goldenrod") #if this is removed, when it runs into itself it doesnt crash
        setPixels(x, y, "goldenrod")
        print("colorchk")
    else:
        moving = False
        print("crash")
        
def setPixels(x, why, color):
    global image
    y = 200 - why
    #top left
    image.setPixel(x-1, y+1, color)
    
    #top center
    image.setPixel(x, y+1, color)
    
    #top right
    image.setPixel(x+1, y+1, color)
    
    #mid left
    image.setPixel(x-1 ,y, color)
    
    #original
    image.setPixel(x, y, color)
    
    #mid right
    image.setPixel(x+1, y, color)
    
    #bot left
    image.setPixel(x-1, y-1, color)
    
    #bot mid
    image.setPixel(x, y-1, color)
    
    #bot right
    image.setPixel(x+1, y-1, color)
       
main()
##EXPERIMENT1
##    while True:
##        char = screen.getch()
##        if char == 113:
##            exit()  # q
##        elif char == curses.KEY_RIGHT:
##            bike.update(RIGHT)
##        #print
##        elif char == curses.KEY_LEFT:
##            bike.update(LEFT)
##        #print
##        elif char == curses.KEY_UP:
##            bike.update(UP)
##        #print
##        elif char == curses.KEY_DOWN:
##            bike.update(DOWN)
##        #print
##        else:
##            bike.update()
##        time.sleep(0.1)
#EXPERIMENT1

#make a list of xy coords and "crash" the program if any of them == eachother
#for i in range(x's):
#   if x == x's[i]
        #for p in range(y's):
            #
