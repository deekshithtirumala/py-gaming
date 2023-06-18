from turtle import Screen, Turtle
import random,time
FONT = ('Arial', 18, 'bold')
runs=False
cruns=False
notout=True
CON=0
def computermove(game):
    global CON
    a=""
    for i in game.enemy:
        if CON==0:
            a=random.choice(["up","down","left","right"])
            CON+=1
        else:
            b=random.choice(["up","down","left","right"])
            CON=0
            if a!=b:
                if a=="up" and b!="down":
                    move(b,i,game)
                    break
                elif a=="left" and b!="right":
                    move(b,i,game)
                    break
                elif a=="right" and b!="left":
                    move(b,i,game)
                    break
                elif a=="down" and b!="up":
                    move(b,i,game)
                    break
                else:
                    b=random.choice(["up","down","left","right"])
            else:
                b=random.choice(["up","down","left","right"])

    computermove(game)
def move(b,postion,game):
    print(postion)
    if b=="up":
        game.enemy[postion].go_up(game)
    elif b=="down":
        game.enemy[postion].go_down(game)
    elif b=="right":
        game.enemy[postion].go_right(game)
    elif b=="left":
        game.enemy[postion].go_left(game)
        

class Creator(Turtle):
    def __init__(self, row, col, sprite, colorcode, width, height, game):
        self.game=game
        super().__init__(shape=sprite)
        self.row = row
        self.col = col
        self.color(colorcode)
        self.shapesize(width, height, 3)
        self.penup()
        self.speed(10)
        self.goto(self.coords(row, col))
    @staticmethod
    def coords(row, col):
        x = col * 25 - 250
        y = 137.5 - row * 25

        return x, y
    
    @staticmethod
    def inv_coords(x, y):
        col = round((x + 250) / 25)
        row = round((137.5 - y) / 25)

        return row, col

    def go_left1(self):
        global runs
        if runs==False:
            runs=True
            position = self.xcor() - 25, self.ycor()

            key = self.inv_coords(*position)

            if key not in self.game.wall:

                if ((key in self.game.food)and(self.game.food[key].isvisible()==True)):
                    self.game.food[key].hideturtle()
                    self.game.score += 1
                    self.game.running.writer.clear()
                    self.game.running.writer.write("score:{}".format(self.game.score), font=FONT)
                    if self.game.score==102:
                        screen.clear()
                        self.game.running.writer.clear()
                        self.game.running.writer.goto(0,0)
                        slef.game.running.writer.write('game over')
                self.goto(self.coords(*key))
            runs=False


    def go_right1(self):
        global runs
        if runs==False:
            runs=True

            position = self.xcor() + 25, self.ycor()

            key = self.inv_coords(*position)

            if key not in self.game.wall:

                if ((key in self.game.food)and(self.game.food[key].isvisible()==True)):
                    self.game.food[key].hideturtle()
                    self.game.score += 1
                    self.game.running.writer.clear()
                    self.game.running.writer.write("score:{}".format(self.game.score), font=FONT)
                    if self.game.score==102:
                        screen.clear()
                        self.game.running.writer.clear()
                        self.game.running.writer.goto(0,0)
                        self.game.running.writer.write('game over')

                self.goto(self.coords(*key))

            runs=False
    def go_up1(self):
        global runs
        if runs==False:
            runs=True

            position = self.xcor(), self.ycor() + 25

            key = self.inv_coords(*position)

            if key not in self.game.wall:

                if ((key in self.game.food)and(self.game.food[key].isvisible()==True)):
                    self.game.food[key].hideturtle()
                    self.game.score += 1
                    self.game.running.writer.clear()
                    self.game.running.writer.write("score:{}".format(self.game.score), font=FONT)
                    if self.game.score==102:
                        screen.clear()
                        self.game.running.writer.clear()
                        self.game.running.writer.goto(0,0)
                        self.game.running.writer.write('game over')
        
                self.goto(self.coords(*key))
            runs=False

    def go_down1(self):
        global runs
        if runs==False:
            runs=True

            position = self.xcor(), self.ycor() - 25

            key = self.inv_coords(*position)

            if key not in self.game.wall:

                if ((key in self.game.food)and(self.game.food[key].isvisible()==True)):
                    self.game.food[key].hideturtle()
                    self.game.score += 1
                    self.game.running.writer.clear()
                    self.game.running.writer.write("score:{}".format(self.game.score), font=FONT)
                    if self.game.score==102:
                        screen.clear()
                        self.game.running.writer.clear()
                        self.game.running.writer.goto(0,0)
                        self.game.running.writer.write('game over')

                self.goto(self.coords(*key))
            runs=False

class Enemy_creator(Turtle):
    def __init__(self, row, col, sprite, colorcode, width, height):
        super().__init__(shape=sprite)
        self.row = row
        self.col = col

        self.color(colorcode)
        self.shapesize(width, height, 3)
        self.penup()
        self.speed('fastest')
        self.goto(self.coords(row, col))

        self.last_key = None
        self.last_dir = None

    @staticmethod
    def coords(row, col):
        x = col * 25 - 250
        y = 137.5 - row * 25

        return x, y

    @staticmethod
    def inv_coords(x, y):
        col = round((x + 250) / 25)
        row = round((137.5 - y) / 25)

        return row, col

    def go_left(self, game):
        global cruns, notout
        if cruns == False:
            cruns = True
            self.game = game
            position = self.xcor() - 25, self.ycor()

            key = self.inv_coords(*position)
            if position == (game.player[9, 9].xcor(), game.player[9, 9].ycor()):
                screen.clear()
                notout = False
            if key not in game.wall:
                self.setheading(0)
                self.goto(self.coords(*key))
            self.last_key = key
            self.last_dir = 2

            cruns = False

    def go_right(self, game):
        global cruns, notout

        if cruns == False:
            cruns = True
            self.game = game

            position = self.xcor() + 25, self.ycor()

            key = self.inv_coords(*position)
            if position == (game.player[9, 9].xcor(), game.player[9, 9].ycor()):
                screen.clear()
                notout = False

            if key not in game.wall:
                self.setheading(180)
                self.goto(self.coords(*key))

            self.last_key = key
            self.last_dir = 3
            cruns = False

    def go_up(self, game):
        global cruns, notout

        if cruns == False:
            cruns = True
            self.game = game

            position = self.xcor(), self.ycor() + 25

            key = self.inv_coords(*position)
            if position == (game.player[9, 9].xcor(), game.player[9, 9].ycor()):
                screen.clear()
                notout = False

            if key not in game.wall:
                self.setheading(90)
                self.goto(self.coords(*key))

            self.last_key = key
            self.last_dir = 0
            cruns = False

    def go_down(self, game):
        global cruns, notout

        if cruns == False:
            cruns = True
            self.game = game

            position = self.xcor(), self.ycor() - 25

            key = self.inv_coords(*position)
            if position == (game.player[9, 9].xcor(), game.player[9, 9].ycor()):
                screen.clear()
                notout = False

            if key not in game.wall:
                self.setheading(-90)
                self.goto(self.coords(*key))
            self.last_key = key
            self.last_dir = 1
            cruns = False
class Running:
    def __init__(self, game):
        self.game = game

        self.writer = Turtle(visible=False)
        self.writer.penup()
        self.writer.color('blue')
        self.writer.goto(200, 170)
        self.writer.write("score:{}".format(game.score), font=FONT)

        screen.onkey(game.player[9, 9].go_left1, 'a')
        screen.onkey(game.player[9, 9].go_right1, 'd')
        screen.onkey(game.player[9, 9].go_up1, 'w')
        screen.onkey(game.player[9, 9].go_down1, 's')
        screen.onkey(self.movingcomputer,'space')
        screen.onkey(self.exit,'q')
        screen.listen()
    def exit(self):
        global notout
        notout=False
        exit()
    def movingcomputer(self):
        while notout:
            computermove(self.game)

class Pacman:
    def __init__(self):
        self.wall = {}
        self.player = {}
        self.food = {}
        self.enemy = {}

        self.score = 0
        screen.tracer(0)
        self.setup()
        screen.tracer(1)
        self.running = Running(self)
    def setup(self):
        for row in range(11):
            for col in range(20):
                if level[row][col] == 1:
                    self.wall[(row, col)] = Creator(row, col, 'square', 'blue', 1, 1, self)
                elif level[row][col] == 2:
                    color=random.choice(['red','green','skyblue','gray'])
                    self.enemy[(row, col)] = Enemy_creator(row, col, 'triangle', color, 1, 1)
                elif level[row][col] == 3:
                    self.player[(row, col)] = Creator(row, col, 'circle', 'yellow', 1, 1, self)
                else:
                    self.food[(row, col)] = Creator(row, col, 'circle', 'white', 0.1, 0.1, self)


level = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 2, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

screen = Screen()
screen.bgcolor('black')
game = Pacman()
screen.mainloop()
