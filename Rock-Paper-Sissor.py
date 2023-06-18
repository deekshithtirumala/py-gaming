import random
from turtle import *
def chose():
    return random.choice(['Paper.gif','Rock.gif','Sissors.gif'])
va=''
ca=''
sa=0
ga=0
running=False
sn=Screen()
sn.tracer(0)
sn.bgcolor('lightGray')
register_shape("Rock.gif")
register_shape("Paper.gif")
register_shape("Sissors.gif")
c=Turtle(visible=False)
c.up()
c.goto(150,0)
c.write(ca,move=False, align="center", font=("Arial", 18, "normal"))
s=Turtle(visible=False)
s.up()
s.goto(140,150)
s.write('computerscore:{}'.format(sa),move=False, align="center", font=("Arial", 18, "normal"))
g=Turtle(visible=False)
g.up()
g.goto(-180,150)
g.write('your score:{}'.format(ga),move=False, align="center", font=("Arial", 18, "normal"))
t=Turtle(visible=False)
t.up()
t.goto(-180,0)
t.write(va,move=False, align="center", font=("Arial", 18, "normal"))
w=Turtle(visible=False)
w.up()
w.goto(0,-200)
w.write('click r:Rock,p:paper,s:sissors and q for exit',move=False, align="center", font=("Arial", 18, "normal"))
def score(a):
    global sa,ga, running
    z=a[0]
    b=a[1]
    ga+=z
    sa+=b
    s.clear()
    s.write('score:{}'.format(sa),move=False, align="center", font=("Arial", 18, "normal"))
    g.clear()
    g.write('score:{}'.format(ga),move=False, align="center", font=("Arial", 18, "normal"))
    if ga==5:
        w.clear()
        ga=0
        sa=0
        w.write('You Won',move=False, align="center", font=("Arial", 18, "normal"))
    elif sa==5:
       w.clear()
       ga=0
       sa=0
       w.write('Computer Won',move=False, align="center", font=("Arial", 18, "normal"))
    else:
        w.clear()
        w.write('click r:Rock,p:paper,s:sissors and q for exit',move=False, align="center", font=("Arial", 18, "normal"))
    running=False
    sn.update()
def judge(x,y):
    a=[]
    if((x=='Paper.gif')and (y=='Rock.gif')):
        a=[1,0]
    elif((x=='Rock.gif')and (y=='Paper.gif')):
        a=[0,1]
    elif((x=='Sissors.gif')and (y=='Paper.gif')):
        a=[1,0]
    elif((x=='Paper.gif')and (y=='Sissors.gif')):
        a=[0,1]
    elif((x=='Rock.gif')and (y=='Sissors.gif')):
        a=[1,0]
    elif((x=='Sissors.gif')and (y=='Rock.gif')):
        a=[0,1]
    else:
        a=[0,0]
    score(a)
def computer(va):
    ca=chose()
    c.showturtle()
    c.shape(ca)
    judge(va,ca)
def paper():
    global running
    if running==False:
        running=True
        va='Paper.gif'
        t.showturtle()
        t.shape('Paper.gif')
        computer(va)
def rock():
    global running
    if running==False:
        running=True
        va='Rock.gif'
        t.showturtle()
        t.shape('Rock.gif')
        computer(va)
def sissors():
    global running
    if running==False:
        running=True
        va='Sissors.gif'
        t.showturtle()
        t.shape('Sissors.gif')
        computer(va)

sn.update()
listen()
onkey(paper,'p')
onkey(rock,'r')
onkey(sissors,'s')
onkey(exit,'q')
'''
class MyTurtle(Turtle):
     def glow(self,x,y):
         self.fillcolor("red")
     def unglow(self,x,y):
         self.fillcolor("")
sn=Screen()
turtle = MyTurtle()
turtle.shape('turtle')
turtle.shapesize(9)
turtle.onclick(turtle.glow)     # clicking on turtle turns fillcolor red,
turtle.onrelease(turtle.unglow)
'''
sn.mainloop()
