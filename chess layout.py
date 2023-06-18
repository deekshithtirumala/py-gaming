import turtle
import os
win=turtle.Screen()
width=619
height=619
win.setup(width,height)
pen=turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.up()
pen.goto(-300,300)
pen.down()
pen.right(90)
count=0
j=75
x=0
def box():
    pen.begin_fill()
    if x%2==0:
        pen.fillcolor('black')
    else :
        pen.fillcolor('white')
    for i in range(5):
        pen.forward(75)
        pen.left(90)
    pen.right(90)
    pen.end_fill()
for i in range (8):
    while count<8:
        box()
        count+=1
        x+=1
    if count==8:
        count=0
        if x%2==0:
            x=1
        else :
            x=0
    z=-300+(i+1)*75
    pen.up()
    pen.goto(z,300)
    pen.down()
