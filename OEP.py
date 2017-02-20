# Tyler Collins and James Gelok
# OEP.py
from turtle import *
from random import randrange
import math

## This program, constructed through the genius of Tyler Collins and James Gelok,
## is a Tron Lightbike survival game. The goal is to move your colored bike around the arena
## without touching your (or your enemy's) trail left behind from the traveling bikes.
## Through using techniques such as encircling your opponent, cutting him/her off, and many others
## you can force your enemy into your or her trail and obtain victory!
##
## This game comes standard with:
##     - 2 bikes:
##         + Goldenrod - controlled using left/right arrow keys
##         + Cyan - controloled using q/w letter keys
##     - large map with boundaries which cause you to die should you hit them
##     - Blow up animations for the bike who hit a light wall
##     - And a brand new INVISIBILITY POWERUP!
##             + After a certain point in the game a purple square will appear
##               on the map. run into it to obtain it and until your next turn your
##               line will be invisible but still there.
##             + Use this to trick and trap your opponents into an invisible wall

def main():
    global bike
    global tron
    global xList
    global yList
    global pX
    global pY = 10
    
    pX = []
    pY = []
    xList = []
    yList = []
    
    #creates border
    bdr = Turtle()
    bdr.speed(0)
    bdr.penup()
    bdr.backward(350)
    bdr.pendown()
    bdr.left(90)
    bdr.forward(350)
    bdr.right(90)
    for i in range(3):
        bdr.forward(700)
        bdr.right(90)
    bdr.forward(350)
    bdr.hideturtle()
# This is a
# Multiline Comment
# I wanna try it
    #creates Goldenrod
    bike = Turtle()
    bike.penup()
    bike.backward(200)
    bike.left(90)
    bike.forward(50)
    bike.right(90)
    bike.pendown()
    bike.pencolor("goldenrod")

    #creates Cyan
    tron = Turtle()
    tron.penup()
    tron.forward(200)
    tron.right(90)
    tron.forward(50)
    tron.right(90)
    tron.pendown()
    tron.pencolor("cyan")

    move()

def getCoords(bike):
    x = bike.xcor()   #int(shape.p2.x - (abs(shape.p1.x - shape.p2.x) / 2))
    y = bike.ycor()   #int(shape.p2.y - (abs(shape.p1.y - shape.p2.y) / 2))
    return x, y
    
def move():
    global bike
    global tron
    global moving

    moving = True
    
    while moving:
        global turn
        global tronTurn
        global pX
        global pY
        
        tron.forward(1)
        bike.forward(1)

        pX, pY = invisibility()
        
        onkey(tronLeft, "q")
        onkey(tronRight, "w")
        onkey(right, "Right")
        onkey(left, "Left")
        listen()
        
        x,y = getCoords(tron)
        colorChk(x, y, tron)

        x,y = getCoords(bike)
        colorChk(x, y, bike)
    #game over text at the end
    go = Turtle()
    go.hideturtle()
    go.penup()
    go.backward(50)
    go.pendown()
    go.pencolor("red")
    go.write("GAME OVER!", font=("Arial", 16, "normal"))

def colorChk(x,y,bike):
    global moving
    global xList
    global yList
    global pX
    global pY
    global inv
    
    #checks to make sure the turtles dont run out of bounds
    if abs(x) > 350 or abs(y) > 350:
        moving = False
        #blow up animation in color of the bike that blows up 
        bike.hideturtle()
        for t in range(12):
                bike.right(30)
                bike.forward(30)
                bike.setposition(x,y)

    #checks if turtle hits other turtle (or own turtle's) trail
    for i in range(len(xList)):
        if x == xList[i] and y == yList[i]: 
            moving = False
            q,p = getCoords(bike)
            #blow up animation in color of the bike that blows up 
            bike.hideturtle()
            for t in range(12):
                bike.right(30)
                bike.forward(30)
                bike.setposition(q,p)
    #invisibility
    for i in range(len(pX)):
        if x == pX[i] and y == pY[i]:
            bike.penup()
            inv.reset()
            inv.hideturtle()
            
    xList.append(x)
    yList.append(y)

def tronRight():
    global tron
    
    tron.down()
    tron.right(90)
    tron.forward(1)

def tronLeft():
    global tron

    tron.down()
    tron.left(90)
    tron.forward(1)
    
def right():
    global bike 

    bike.down()
    bike.right(90)
    bike.forward(1)
    
def left():
    global bike

    bike.down()
    bike.left(90)
    bike.forward(1)

def invisibility():
    #Tyler
    global bike
    global tron
    global pX
    global pY
    global xList
    global inv
    
    x = randrange(-340, 340, 1)
    y = randrange(-340, 340, 1)
    #activates powerup after turtle reaches a certain length (can happen multiple times)
    if (len(xList) % 1500 == 0) and (len(xList) != 0):
        inv = Turtle()
        inv.pencolor("purple")
        inv.hideturtle()
        inv.penup()
        inv.setposition(x,y)
        inv.pendown()
        pX.append(x)
        pY.append(y)
        #draws the powerup
        for p in range(4):
            for i in range(8):
                inv.forward(1)
                x,y = getCoords(inv)
                pX.append(x)
                pY.append(y)
            inv.right(90)
        #returns the list of coordinates the powerup takes up
        return pX, pY
    else:
        return pX, pY
    
main()

## Bugs: The only bug that we have found is rarely the bike will slip between the x,y coordinates
## that make up the trail. This bug has been a unfixable since the beginning.
