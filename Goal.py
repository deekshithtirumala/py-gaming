from turtle import *
import random
class Football(Turtle):
    def __init__(self,game):
        super().__init__(shape='circle')
        self.game=game
        self.color('white')
        self.shapesize(1.5,1.5,None)
        self.pu()
class Line(Turtle):
    def __init__(self,game):
        super().__init__(shape='square')
        self.game=game
        self.shapesize(0.05,30,None)
        self.pu()
        self.goto(0,220)
        self.pu()
class Player(Turtle):
    def __init__(self,game):
        super().__init__(shape='square')
        self.game=game
        self.pu()
        self.shapesize(0.5, 4, None)
        self.goto(0,230)
    def move_left(self):
        onkey(None,'a')
        self.x_present=self.xcor()
        if ((self.x_present-30)>-280):
            self.goto((self.x_present-30),230)
        onkey(self.game.player.move_left,'a')
    def move_right(self):
        onkey(None,'d')
        self.x_present=self.xcor()
        if ((self.x_present+30)<280):
            self.goto((self.x_present+30),230)
        onkey(self.game.player.move_right,'d')
class Controller:
    def __init__(self, game):
        self.game=game
        self.setup()
    def setup(self):
        self.writer=Turtle(visible=False)
        self.writer.pu()
        self.writer.goto(0,-150)
        self.writer.pencolor('red')
        self.writer.write('Press space to kick the Ball',align='center',font=('Arial',18,'bold'))
        onkey(self.start,'space')
        onkey(self.game.player.move_left,'a')
        onkey(self.game.player.move_right,'d')
        listen()
    def checker(self):
        if(self.game.ball.xcor()<(self.game.player.xcor()+30))and(self.game.ball.xcor()>(self.game.player.xcor()-30)):
            self.writer.clear()
            self.writer.write('Yaaa! You Stopped Goal',align='center',font=('Arial',18,'bold'))
        else:
            self.writer.clear()
            self.writer.write('you failed stopping the goal',align='center',font=('Arial',18,'bold'))
    def start(self):
        angle=random.randint(60,120)
        self.game.ball.setheading(angle)
        while self.game.running:
            onkey(None,'space')
            if self.game.ball.ycor()>240:
                win.tracer(0)
                self.checker()
                self.game.ball.goto(0,0)
                win.tracer(1)
                onkey(self.start,'space')
                break
            self.game.ball.forward(5)
            onkey(self.start,'space')

class Main:
    def __init__(self):
        self.running=True
        win.tracer(0)
        self.setup()
        self.control=Controller(self)
        win.tracer(1)
    def setup(self):
        self.draw()
        self.ball=Football(self)
        self.goal_line=Line(self)
        self.player=Player(self)
    def draw(self):
        self.net=Turtle(visible=False)
        self.net.pensize(15)
        self.net.pencolor((80,80,85))
        self.net.pu()
        self.net.goto(-150,240)
        self.net.down()
        self.net.goto(-150,290)
        self.net.forward(300)
        self.net.goto(150,240)
win=Screen()
win.setup(640,600)
win.colormode(255)
win.bgcolor((202,164,114))
Main()
win.mainloop()
