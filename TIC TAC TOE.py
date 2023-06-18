from turtle import *
win=Screen()
j=0#person name if 0 for 'x' and 1 for 'o'
win.colormode(255)
win.bgcolor((20,189,172))
bgdrawer=Turtle(visible=False)# writer of 'x' or 'o'
bgdrawer.pensize(10)
bgdrawer.pencolor('grey')
bgdrawer.up()
win.tracer(0)
bgdraw=Turtle(visible=False)#lines drawing
bgdraw.pensize(10)
bgdraw.pencolor((83,83,83))
notify=Turtle(visible=False)#the text you see down
notify.up()
notify.goto(0,-180)

#names of plces
a1=0
a2=0
a3=0
a4=0
a5=0
a6=0
a7=0
a8=0
a9=0
def ngame():#new game
    global a1,a2,a3,a4,a5,a6,a7,a8,a9
    bgdrawer.clear()
    notify.clear()
    a1=0
    a2=0
    a3=0
    a4=0
    a5=0
    a6=0
    a7=0
    a8=0
    a9=0
    notify.write('Ok'.format(a1),move=False, align="center", font=("Arial", 18, "normal"))
    initalizer()
def initalizer():
    global j
    if j==0:
        listen()
        win.onclick(anlyser)
        j=1
    elif j==1:
        listen()
        win.onclick(anlyser)
        j=0
def chek():#to veryify there is a winner our not
    global a1,a2,a3,a4,a5,a6,a7,a8,a9
    if ((a1==a2 and a2==a3)or(a1==a4 and a4==a7)or(a1==a5 and a5==a9))and(a1!=0):
        notify.clear()
        notify.write('{} is the winner and press space for start'.format(a1),move=False, align="center", font=("Arial", 18, "normal"))
        listen()
        onkey(ngame,'space')
        win.onclick(None)
    elif (a4==a5 and a5==a6)and(a4!=0):
        notify.clear()
        notify.write('{} is the winner and press space for start'.format(a4),move=False, align="center", font=("Arial", 18, "normal"))
        listen()
        onkey(ngame,'space')
        win.onclick(None)
    elif ((a7==a8 and a8==a9)or(a7==a5 and a5==a3))and(a7!=0):
        notify.clear()
        notify.write('{} is the winner and press space for start'.format(a7),move=False, align="center", font=("Arial", 18, "normal"))
        listen()
        win.onclick(None)
        onkey(ngame,'space')
    elif (a2==a5 and a5==a8)and(a2!=0):
        notify.clear()
        notify.write('{} is the winner and press space for start'.format(a2),move=False, align="center", font=("Arial", 18, "normal"))
        listen()
        onkey(ngame,'space')
        win.onclick(None)
    elif (a3==a6 and a6==a9)and(a3!=0):
        notify.clear()
        notify.write('{} is the winner and press space for start'.format(a3),move=False, align="center", font=("Arial", 18, "normal"))
        listen()
        onkey(ngame,'space')
        win.onclick(None)
    elif (a1!=0 and a2!=0 and a3!=0 and a4!=0 and a5!=0 and a6!=0 and a7!=0 and a8!=0 and a9!=0):
        ngame()
    else:
        initalizer()
def bg():#fuction to draw lines
    bgdraw.up()
    bgdraw.goto(-150,50)
    bgdraw.down()
    bgdraw.goto(150,50)
    bgdraw.up()
    bgdraw.goto(-150,-50)
    bgdraw.down()
    bgdraw.goto(150,-50)
    bgdraw.up()
    bgdraw.goto(-50,150)
    bgdraw.down()
    bgdraw.goto(-50,-150)
    bgdraw.up()
    bgdraw.goto(50,150)
    bgdraw.down()
    bgdraw.goto(50,-150)
    bgdraw.up()
    win.tracer(0)
def score(x,y):#changing value
    global j,a1,a2,a3,a4,a5,a6,a7,a8,a9
    if j==0:
        bgdrawer.pencolor('grey')
        if x==1:#x=2 o=1
            a1='X'
        elif x==2:
            a2='X'
        elif x==3:
            a3='X'
        elif x==4:
            a4='X'
        elif x==5:
            a5='X'
        elif x==6:
            a6='X'
        elif x==7:
            a7='X'
        elif x==8:
            a8='X'
        elif x==9:
            a9='X'
        chek()
    elif j==1:
        bgdrawer.pencolor('White')
        if x==1:#x=2 o=1
            a1='O'
        elif x==2:
            a2='O'
        elif x==3:
            a3='O'
        elif x==4:
            a4='O'
        elif x==5:
            a5='O'
        elif x==6:
            a6='O'
        elif x==7:
            a7='O'
        elif x==8:
            a8='O'
        elif x==9:
            a9='O'
        chek()
def draw(a):#going to that positon  and writing x and o 
    global j,a1,a2,a3,a4,a5,a6,a7,a8,a9
    if a==1:
    	if a1==0:
	        bgdrawer.goto(-100,46)
	        if j==0:
	            bgdrawer.write('X',move=False, align="center", font=("Arial", 72, "normal"))
	            score(a,'x')
	            j=1
	        elif j==1:
	            bgdrawer.write('O',move=False, align="center", font=("Arial", 72, "normal"))
	            score(a,'o')
	            j=0
    elif a==2:
    	if a2==0:
	        bgdrawer.goto(0,46)
	        if j==0:
	            bgdrawer.write('X',move=False, align="center", font=("Arial", 72, "normal"))
	            score(a,'x')
	            j=1
	        elif j==1:
	            bgdrawer.write('O',move=False, align="center", font=("Arial", 72, "normal"))
	            score(a,'o')
	            j=0
    elif a==3:
    	if a3==0:
	        bgdrawer.goto(100,46)
	        if j==0:
	            bgdrawer.write('X',move=False, align="center", font=("Arial", 72, "normal"))
	            score(a,'x')
	            j=1
	        elif j==1:
	            bgdrawer.write('O',move=False, align="center", font=("Arial", 72, "normal"))
	            score(a,'o')
	            j=0
    elif a==4:
    	if a4==0:
	        bgdrawer.goto(-100,-56)
	        if j==0:
	            bgdrawer.write('X',move=False, align="center", font=("Arial", 72, "normal"))
	            score(a,'x')
	        elif j==1:
	            bgdrawer.write('O',move=False, align="center", font=("Arial", 72, "normal"))
	            score(a,'o')
	            j=0
    elif a==5:
    	if a5==0:
	        bgdrawer.goto(0,-56)
	        if j==0:
	            bgdrawer.write('X',move=False, align="center", font=("Arial", 72, "normal"))
	            score(a,'x')
	            j=1
	        elif j==1:
	            bgdrawer.write('O',move=False, align="center", font=("Arial", 72, "normal"))
	            score(a,'o')
	            j=0
    elif a==6:
    	if a6==0:
	        bgdrawer.goto(100,-56)
	        if j==0:
	            bgdrawer.write('X',move=False, align="center", font=("Arial", 72, "normal"))
	            score(a,'x')
	            j=1
	        elif j==1:
	            bgdrawer.write('O',move=False, align="center", font=("Arial", 72, "normal"))
	            score(a,'o')
	            j=0
    elif a==7:
    	if a7==0:
	        bgdrawer.goto(-100,-156)
	        if j==0:
	            bgdrawer.write('X',move=False, align="center", font=("Arial", 72, "normal"))
	            score(a,'x')
	            j=1
	        elif j==1:
	            bgdrawer.write('O',move=False, align="center", font=("Arial", 72, "normal"))
	            score(a,'o')
	            j=0
    elif a==8:
    	if a8==0:
	        bgdrawer.goto(0,-156)
	        if j==0:
	            bgdrawer.write('X',move=False, align="center", font=("Arial", 72, "normal"))
	            score(a,'x')
	            j=1
	        elif j==1:
	            bgdrawer.write('O',move=False, align="center", font=("Arial", 72, "normal"))
	            score(a,'o')
	            j=0
    elif a==9:
    	if a9==0:
	        bgdrawer.goto(100,-156)
	        if j==0:
	            bgdrawer.write('X',move=False, align="center", font=("Arial", 72, "normal"))
	            score(a,'x')
	            j=1
	        elif j==1:
	            bgdrawer.write('O',move=False, align="center", font=("Arial", 72, "normal"))
	            score(a,'o')
	            j=0
def anlyser(x,y):# know where the player tapped
    if ((x>-150 and x<-50)and(y<150 and y>50)):
        notify.clear()
        notify.write('',move=False, align="center", font=("Arial", 18, "normal"))
        draw(1)
    elif ((x>-50 and x<50)and(y<150 and y>50)):
        notify.clear()
        notify.write('',move=False, align="center", font=("Arial", 18, "normal"))
        draw(2)
    elif ((x>50 and x<150)and(y<150 and y>50)):
        notify.clear()
        notify.write('',move=False, align="center", font=("Arial", 18, "normal"))
        draw(3)
    elif ((x>-150 and x<-50)and(y<50 and y>-50)):
        notify.clear()
        notify.write('',move=False, align="center", font=("Arial", 18, "normal"))
        draw(4)
    elif ((x>-50 and x<50)and(y<50 and y>-50)):
        notify.clear()
        notify.write('',move=False, align="center", font=("Arial", 18, "normal"))
        draw(5)
    elif ((x>50 and x<150)and(y<50 and y>-50)):
        notify.clear()
        notify.write('',move=False, align="center", font=("Arial", 18, "normal"))
        draw(6)
    elif ((x>-150 and x<-50)and(y<-50 and y>-150)):
        notify.clear()
        notify.write('',move=False, align="center", font=("Arial", 18, "normal"))
        draw(7)
    elif ((x>-50 and x<50)and(y<-50 and y>-150)):
        notify.clear()
        notify.write('',move=False, align="center", font=("Arial", 18, "normal"))
        draw(8)
    elif ((x>50 and x<150)and(y<-50 and y>-150)):
        notify.clear()
        notify.write('',move=False, align="center", font=("Arial", 18, "normal"))
        draw(9)
    else:
        notify.write('Please Select Valid',move=False, align="center", font=("Arial", 18, "normal"))
bg()#to create BACKGROUNG
initalizer()#starting game
win.mainloop()
