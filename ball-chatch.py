from turtle import *
import random
import paho.mqtt.client as mqtt
import time
import json
import random

host='mqtt.dioty.co'
key='theworkers2020@gmail.com'
password='c4bf45a8'
client=mqtt.Client()
client.username_pw_set(username=key,password=password)
client.connect(host,1883,60)


s=Screen()
sa=0
verifyer=False
x_cor="center"
s.setworldcoordinates(-340,-340,340,340)
gameboard=Turtle(visible=False)
gameboard.pensize(1)
gameboard.pu()
gameboard.goto(-320,320)
gameboard.down()
s.tracer(False)
for i in range(4):
    gameboard.forward(640)
    gameboard.right(90)
s.tracer(True)
s.bgcolor('lightgray')
bowl=Turtle('square')
bowl.up()
bowl.goto(0,-200)
ball=Turtle(visible=False)
ball.up()
ball.speed(0)
ball.shape('circle')
ball.shapesize(0.3,0.3,0)
ball.goto(-100,200)
ball.showturtle()
notify=Turtle(visible=False)
notify.up()
score=Turtle(visible=False)
score.up()
score.goto(180,230)
score.write('Score:{}'.format(sa),move=False, align="center", font=("Arial", 18, "normal"))
def chose():
    lst=[]
    for i in range(13):
        a=(i-6)*50
        lst.append(a)
    return random.choice(lst)
def left():
    x=bowl.xcor()
    x-=50
    if x>-320:
        bowl.setx(x)
    else :
        s.tracer(False)
        bowl.goto(300,-200)
        s.tracer(True)
def checker():
    global sa
    a=ball.xcor()
    b=ball.ycor()
    c=bowl.xcor()
    d=bowl.ycor()
    if ((c+20>a and c-20<a) and (d<b and d+6>b)):
        ball.hideturtle()
        sa+=1
        score.clear()
        score.write('Score:{}'.format(sa),move=False, align="center", font=("Arial", 18, "normal"))   
        x=chose()
        ball.goto(x,200)
        ball.showturtle()
def right():
    x=bowl.xcor()
    x+=50
    if x<320:
        bowl.setx(x)
    else :
        s.tracer(False)
        bowl.goto(-300,-200)
        s.tracer(True)
def restart():
    notify.clear()
    score.write('Score:{}'.format(sa),move=False, align="center", font=("Arial", 18, "normal"))
    bowl.showturtle()
    x=chose()
    ball.goto(x,200)
    ball.showturtle()
    running=True
    run()
def run():
    global running,active,x_cor,verifyer
    while running:
        
        y=ball.ycor()
        if verifyer==True:
            if x_cor[0]=="left":
                left()
            elif x_cor[0]=="right":
                right()
            verifyer=False
        else:
            y-=1
            ball.sety(y)
        checker()
        if y<-250:
            ball.hideturtle()
            running=False
            bowl.hideturtle()
            notify.write('Game Over and press space to Restart',move=False, align="center", font=("Arial", 18, "normal"))
def again():
    global running,sa
    if running==True:
        return
    else:
        ball.goto(0,200)
        sa=0
        score.clear()
        restart()
        bowl.showturtle()
        running=True
        run()
def msg(client,userdata,msg):
    global x_cor,verifyer
    x_cor=str(msg.payload.decode("utf-8")).split()
    verifyer=True
    try:
        if len(x_cor)==1:
            print(x_cor)
    except Exception as e:
        print("no data")

client.subscribe('/theworkers2020@gmail.com/joy')
client.on_message=msg
client.loop_start()
listen()

onkey(left,'a')
onkey(right,'d')
onkey(again,'space')
running=True
active=False
run()
s.mainloop()
