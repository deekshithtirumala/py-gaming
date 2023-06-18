from turtle import *
s=Screen()
s.bgcolor('lightgray')
for i in range(10):
    register_shape('taj{}.gif'.format(i))
img=Turtle()
img.up()
img.shape('taj0.gif')
img.shapesize(6,6,1)
img.goto(220,200)
a1=Turtle()
a1.shape('taj5.gif')
a1.up()
a1.goto(-100,100)
a2=Turtle()
a2.shape('taj7.gif')
a2.up()
a2.goto(0,100)
a3=Turtle()
a3.shape('taj6.gif')
a3.up()
a3.goto(100,100)
a4=Turtle()
a4.shape('taj3.gif')
a4.up()
a4.goto(-100,0)
a5=Turtle()
a5.shape('taj2.gif')
a5.up()
a5.goto(0,0)
a6=Turtle()
a6.shape('taj4.gif')
a6.up()
a6.goto(100,0)
a7=Turtle()
a7.shape('taj8.gif')
a7.up()
a7.goto(-100,-100)
a8=Turtle()
a8.shape('taj1.gif')
a8.up()
a8.goto(0,-100)
a9=Turtle()
a9.shape('taj9.gif')
a9.color('gray')
a9.up()
a9.goto(100,-100)
notify=Turtle(visible=False)
notify.up()
notify.goto(0,-200)
def winner():
    j=0
    if (a1.xcor()==0 and a1.ycor()==0):
        j+=1
    if (a2.xcor()==-100 and a2.ycor()==-100):
        j+=1
    if (a3.xcor()==0 and a3.ycor()==100):
        j+=1
    if (a4.xcor()==100 and a4.ycor()==100):
        j+=1
    if (a5.xcor()==0 and a5.ycor()==100):
        j+=1
    if (a6.xcor()==-100 and a6.ycor()==0):
        j+=1
    if (a7.xcor()==0 and a7.ycor()==-100):
        j+=1
    if (a8.xcor()==-100 and a8.ycor()==100):
        j+=1
    if (a9.xcor()==100 and a9.ycor()==-100):
        j+=1
    if j==8:
        notify.clear()
        notify.write('winner',move=False, align="center", font=("Arial", 18, "normal"))
    else:
        notify.clear()
        notify.write('Try Agin some mismatches',move=False, align="center", font=("Arial", 18, "normal"))
def checker(x,y):
    j=0
    if x==a1.xcor() and y==a1.ycor():
        return a1
    elif x==a2.xcor() and y==a2.ycor():
        return a2
    elif x==a3.xcor() and y==a3.ycor():
        return a3
    elif x==a4.xcor() and y==a4.ycor():
        return a4
    elif x==a5.xcor() and y==a5.ycor():
        return a5
    elif x==a6.xcor() and y==a6.ycor():
        return a6
    elif x==a7.xcor() and y==a7.ycor():
        return a7
    elif x==a8.xcor() and y==a8.ycor():
        return a8
    else:
        notify.clear()
        notify.write('Please select valid move',move=False, align="center", font=("Arial", 18, "normal"))
def left():
    global a9
    x=a9.xcor()
    y=a9.ycor()
    k=x-100
    j=y
    z=checker(k,j)
    if str(type(z))=="<class 'turtle.Turtle'>":
        d=z.xcor()
        f=z.ycor()
        a9.goto(d,f)
        z.goto(x,y)
def right():
    global a9
    x=a9.xcor()
    y=a9.ycor()
    k=x+100
    j=y
    z=checker(k,j)
    if str(type(z))=="<class 'turtle.Turtle'>":
        d=z.xcor()
        f=z.ycor()
        a9.goto(d,f)
        z.goto(x,y)
def up():
    global a9
    x=a9.xcor()
    y=a9.ycor()
    k=x
    j=y+100
    z=checker(k,j)
    if str(type(z))=="<class 'turtle.Turtle'>":
        d=z.xcor()
        f=z.ycor()
        a9.goto(d,f)
        z.goto(x,y)
def down():
    global a9
    x=a9.xcor()
    y=a9.ycor()
    k=x
    j=y-100
    z=checker(k,j)
    if str(type(z))=="<class 'turtle.Turtle'>":
        d=z.xcor()
        f=z.ycor()
        a9.goto(d,f)
        z.goto(x,y)
listen()
onkey(left,'a')
onkey(right,'d')
onkey(up,'w')
onkey(down,'s')
onkey(winner,'space')
s.mainloop()
