import turtle
win=turtle.Screen()
      
t0=turtle.Turtle()
t0.shape("circle")
t0.color("white")
t0.pencolor("black")
t0.up()
t1=turtle.Turtle()
t1.shape("circle")
t1.color("black")
t1.pencolor("black")
t1.up()
t2=turtle.Turtle()
t2.shape("circle")
t2.color("black")
t2.pencolor("black")
t2.up()
t3=turtle.Turtle()
t3.shape("circle")
t3.color("black")
t3.pencolor("black")
t3.up()
t4=turtle.Turtle()
t4.shape("circle")
t4.color("black")
t4.pencolor("black")
t4.up()
t5=turtle.Turtle()
t5.shape("circle")
t5.color("black")
t5.pencolor("black")
t5.up()
t6=turtle.Turtle()
t6.shape("circle")
t6.color("black")
t6.pencolor("black")
t6.up()
t7=turtle.Turtle()
t7.shape("circle")
t7.color("black")
t7.pencolor("black")
t7.up()
t8=turtle.Turtle()
t8.shape("circle")
t8.color("black")
t8.pencolor("black")
t8.up()
t9=turtle.Turtle()
t9.shape("circle")
t9.color("red")
t9.pencolor("orange")
t9.up()
#placing on positions
t1.goto(40,0)
t2.goto(80,0)
t3.goto(0,40)
t4.goto(0,80)
t5.goto(-40,0)
t6.goto(-80,0)
t7.goto(0,-40)
t8.goto(0,-80)
t9.goto(0,-150)
#varabiles
text_display='Welcome to game'
x1=0,
y1=0,
x2=0,
y2=0,
lst_b=['t1','t2','t3','t4','t5','t6','t7','t8']
lst_w=['t0']
f_t=0
s_t=0
c_t=0
j=0
#functions
def final_move():
    global f_t,c_t,s_t
    f_txt='+f_t+'
    s_txt='+s_t+'
    c_txt='+c_t+'
    f_t.color('white')
    s_t.color('black')
    c_t.color('white')
    lst_b.remove(f_txt)
    lst_b.remove(c_txt)
    lst_w.remove(s_txt)
    lst_w.append(f_txt)
    lst_w.append(c_txt)
    lst_b.append(s_txt)
    j=0
def check3(a,b):
    global c_t
    x3=a
    y3=b
    if (x3==0 and y3==0):
        c_t=t0
        final_move
    elif (x3==40 and y3==0):
        c_t=t1
        final_move
    elif (x3==80 and y3==0):
        c_t=t2
        final_move
    elif (x3==0 and y3==40):
        c_t=t3
        final_move
    elif (x3==0 and y3==80):
        c_t=t4
        final_move
    elif (x3==-40 and y3==0):
        c_t=t5
        final_move
    elif (x3==-80 and y3==0):
        c_t=t6
        final_move
    elif (x3==0 and y3==-40):
        c_t=t7
        final_move
    elif (x3==0 and y3==-80):
        c_t=t8
        final_move
    else:
        text_display('please Select Other Marble')
def move_one(a):
    if a.color=='black':
        global f_t
        x1=a.xcor()
        y1=a.ycor()
        f_t=a
        j+=0
    else:
        text_display('please Select Other Marble')
def move_two(a):
    if a.color=='white':
        global s_t
        x2=a.xcor()
        y2=a.ycor()
        s_t=a
        x3=(x1+x2)/2
        y3=(y1+y2)/2
        check3(x3,y3)
    else:
        j=0
def check1(a):
    x=a
    y=str(x)
    for i in range(8):
        if lst_b[i]==y:
            move_one(x)
            global text_dislay
            text_display='Select other'
        else:
            text_display='Please select other marble'
def check2(a):
    x=a
    y=str(x)
    for i in lst_w:
        if lst_w[i]==y:
            move_two(x)
            text_display='Ok....'
        else:
            text_display='Please select other marble'
# welcome text
t9.color('orange')    
t9.write(text_display,True,'center',('Arial',24,'normal'))
t9.hideturtle()
turtle.listen()
if j==0:
    turtle.onkey(check1(t0),'a')
    turtle.onkey(check1(t1),'b')
    turtle.onkey(check1(t2),'c')
    turtle.onkey(check1(t3),'d')
    turtle.onkey(check1(t4),'e')
    turtle.onkey(check1(t5),'f')
    turtle.onkey(check1(t6),'g')
    turtle.onkey(check1(t7),'h')
    turtle.onkey(check1(t8),'i')
elif j==1:
    turtle.onkey(check2(t0),'a')
    turtle.onkey(check2(t1),'b')
    turtle.onkey(check2(t2),'c')
    turtle.onkey(check2(t3),'d')
    turtle.onkey(check2(t4),'e')
    turtle.onkey(check2(t5),'f')
    turtle.onkey(check2(t6),'g')
    turtle.onkey(check2(t7),'h')
    turtle.onkey(check2(t8),'i')
win.mainloop()
