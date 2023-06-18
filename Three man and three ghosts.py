from turtle import *


class Creator(Turtle):
    def __init__(self,game, color_code,width,height, x, y):
        Turtle.__init__(self,shape="square")
        self.game=game
        self.beach='right'
        self.pu()
        self.shapesize(height,width,None)
        self.color(color_code)
        self.goto(x, y)
    def move(self, clicked_x,clicked_y):
        for sprites in self.game.player.values():
            sprites.onclick(None)

        if (self.xcor()==150) or (self.xcor()==-150):
            if self.game.person==0 and self.game.beach=='right':
                if self.xcor()>0:
                    self.game.person+=1
                    x,y=(self.game.boat.xcor()-15),self.game.boat.ycor()
                    self.game.in_boat.append(self)
                    self.game.y1=self.ycor()
                    self.goto(x,y)
            elif self.game.person==1 and self.game.beach=='right':
                if self.xcor()>0:
                    self.game.person+=1
                    x,y=(self.game.boat.xcor()+15),self.game.boat.ycor()
                    self.game.in_boat.append(self)
                    self.game.y2=self.ycor()
                    self.goto(x,y)
            
            elif self.game.person==0 and self.game.beach=='left':
                if self.xcor()<0:
                    self.game.person+=1
                    x,y=(self.game.boat.xcor()-15),self.game.boat.ycor()
                    self.game.in_boat.append(self)
                    self.game.y1=self.ycor()
                    self.goto(x,y)
                
            elif self.game.person==1 and self.game.beach=='left':
                if self.xcor()<0:
                    self.game.person+=1
                    x,y=(self.game.boat.xcor()+15),self.game.boat.ycor()
                    self.game.in_boat.append(self)
                    self.game.y2=self.ycor()
                    self.goto(x,y)
            
        for sprites in self.game.player.values():
            sprites.onclick(sprites.move)
    def verify(self):
        left_p=0
        right_p=0
        left_g=0
        right_g=0
        for sprites in self.game.player.values():
            if sprites.beach=='left':
                left_p+=1
            else:
                right_p+=1
        for sprites in self.game.ghosts.values():
            if sprites.beach=='left':
                left_g+=1
            else:
                right_g+=1
        
        if right_p<right_g and (right_p and right_g !=0):
            self.game.control.writer.clear()
            print('yhru')
            self.game.control.writer.write("Game_over press Space to restart",move=False,font=('Arial',18,'bold'),align='center')
            self.game.game_over=True
            for sprites in self.game.player.values():
                sprites.onclick(None)
            for sprites in self.game.ghosts.values():
                sprites.onclick(None)
        elif left_p<left_g and (left_p and left_p !=0):
            self.game.control.writer.clear()
            self.game.control.writer.write("Game_over press Space to restart",move=False,font=('Arial',18,'bold'),align='center')
            self.game.game_over=True
            for sprites in self.game.player.values():
                sprites.onclick(None)
            for sprites in self.game.ghosts.values():
                sprites.onclick(None)
        if left_p==3 and left_g==3:
            self.game.control.writer.clear()
            self.game.control.writer.write("Game_over and your are winner press Space to restart",move=False,font=('Arial',18,'bold'),align='center')
            self.game.game_over=True
            for sprites in self.game.player.values():
                sprites.onclick(None)
            for sprites in self.game.ghosts.values():
                sprites.onclick(None)
    def move_boat(self,click_x,clicked_y):
        button=self.game.button
        button.onclick(None)
        if len(self.game.in_boat)==2:
            if self.game.person==2:
                win.tracer(0)
                go_x=-self.game.boat.xcor()
                self.game.boat.goto(go_x,0)
                self.game.in_boat[0].goto((self.game.boat.xcor()-15),self.game.boat.ycor())
                self.game.in_boat[1].goto((self.game.boat.xcor()+15),self.game.boat.ycor())
                if self.game.boat.xcor()>0:
                    self.game.beach="right"
                    self.game.in_boat[0].goto((150),self.game.y1)
                    self.game.in_boat[1].goto((150),self.game.y2)
                    self.game.in_boat[0].beach='right'
                    self.game.in_boat[1].beach='right'
                else:
                    self.game.beach="left"
                    self.game.in_boat[0].goto((-150),self.game.y1)
                    self.game.in_boat[1].goto((-150),self.game.y2)
                    self.game.in_boat[0].beach='left'
                    self.game.in_boat[1].beach='left'
                self.game.person=0
                self.game.in_boat=[]
                win.tracer(1)
        elif len(self.game.in_boat)==1:
            win.tracer(0)
            go_x=-self.game.boat.xcor()
            self.game.boat.goto(go_x,0)
            self.game.in_boat[0].goto((self.game.boat.xcor()-15),self.game.boat.ycor())
            #self.game.in_boat[1].goto((self.game.boat.xcor()+15),self.game.boat.ycor())
            if self.game.boat.xcor()>0:
                self.game.beach="right"
                self.game.in_boat[0].goto((150),self.game.y1)
                self.game.in_boat[0].beach='right'
                #self.game.in_boat[1].goto((150),self.game.y2)
            else:
                self.game.beach="left"
                self.game.in_boat[0].goto((-150),self.game.y1)
                self.game.in_boat[0].beach='left'
                #self.game.in_boat[1].goto((-150),self.game.y2)
            self.game.person=0
            self.game.in_boat=[]
            win.tracer(1)
        if self.game.in_boat!=0:
            self.verify()
        button.onclick(button.move_boat)
class Controller:
    def __init__(self,game):
        self.game=game
        self.setup()
    def setup(self):
        button=self.game.button
        self.writer=Turtle(visible=False)
        self.writer.pu()
        self.writer.goto(0,-300)
        for sprites in self.game.player.values():
            sprites.onclick(sprites.move)
        for sprites in self.game.ghosts.values():
            sprites.onclick(sprites.move)
        button.onclick(button.move_boat)
class main:
    def __init__(self):
        self.wall={}
        self.river={}
        self.beach="right"#for right side
        self.in_boat=[]#list of name of people present in boat
        self.person=0#for leftside place in boat
        self.player={}
        self.ghosts={}
        self.game_over=False
        self.y1=0
        self.y2=0
        self.left=[]
        self.right=[]
        self.setup()
        self.control=Controller(self)
    
    def setup(self):
        win.tracer(0)#false
        self.river[(0,0)]= Creator(self,(174,214,241),10,20,0,0)
        self.wall[(0,0)]=Creator(self,(135,54,0),5,20,-150,0)
        self.wall[(0,1)]=Creator(self,(135,54,0),5,20,150,0)
        self.boat=Creator(self,(229,152,102),2.5,1.5,75,0)
        self.button=Creator(self,(200,182,190),2.5,1.5,0,-250)
        for row in range(2):
            for col in range(3):
                
                if row==0:
                    y=40+(col*40)
                    self.player[(row,col)]=Creator(self,(213,219,219),1,1,150,y)
                else:
                    y=-40-(col*40)
                    self.ghosts[(row,col)]=Creator(self,(46,64,83),1,1,150,y)
        win.tracer(1)
win=Screen()
win.colormode(255)
win.setup(800,640)

main()
win.mainloop()
