from turtle import *


class Tile(Turtle):
    def __init__(self, game, row, col):
        super().__init__(shape="square")
        self.game=game
        self.row= row
        self.col=col
        self.color_value="black"
        self.shapesize(5,5,None)#1 unit of length is = 20 pixls
        x, y= self.coords(row, col)
        self.up()
        self.goto(x, y)
    def change_color(self, x, y):
        #x, y are postion of clicked but now not requried
        if self.game.player==0:
            if (self.xcor(),self.ycor())not in self.game.over:
                self.color("red")
                
                self.game.player+=1
                self.color_value="red" #we denoting red color by text
                self.verify()
        else:
            self.color("blue")
            self.game.player=0
            self.color_value="blue"
            self.verify()
        self.game.over.append((lambda : (self.xcor()+110)/110,lambda : (110-self.ycor())/110))
    def coords(self, row, col):
        x=(-110+row*110)
        y=(110-col*110)
        return x,y
    def verify(self):
        
        cheker_lst=[] 
        C_N=0#constant
        for tiles in self.game.tile.values():
            cheker_lst.append(tiles.color_value)
        for i in range(3):
            if (cheker_lst[C_N]==cheker_lst[C_N+1])and(cheker_lst[C_N+1]==cheker_lst[C_N+2])and(cheker_lst[C_N]!="black"):
                self.game.control.writer.write("{} is the winner".format(cheker_lst[C_N]),move=False,font=('Arial',18,"bold"))
                
            C_N+=3
        C_N=0
        for i in range(3):
            if (cheker_lst[C_N]==cheker_lst[C_N+3])and(cheker_lst[C_N+3]==cheker_lst[C_N+6])and(cheker_lst[C_N]!="black"):
                self.game.control.writer.write("{} is the winner".format(cheker_lst[C_N]),move=False,font=('Arial',18,"bold"),align="center")
            C_N+=1
        C_N=0
        
        if (cheker_lst[C_N]==cheker_lst[C_N+4])and(cheker_lst[C_N+4]==cheker_lst[C_N+8])and(cheker_lst[C_N]!="black"):
            self.game.control.writer.write("{} is the winner".format(cheker_lst[C_N]),move=False,font=('Arial',18,"bold"),align="center")
        C_N+=2
        if (cheker_lst[C_N]==cheker_lst[C_N+2])and(cheker_lst[C_N+2]==cheker_lst[C_N+4])and(cheker_lst[C_N]!="black"):
            self.game.control.writer.write("{} is the winner".format(cheker_lst[C_N]),move=False,font=('Arial',18,"bold"),align="center")
        
        cheker_lst=[]


class controller:
    def __init__(self,game):
        self.game=game
        self.notice()
        self.setup()
    def notice(self):
        self.writer=Turtle(visible=False)
        self.writer.pu()
        self.writer.goto(0,-200)
        
    def setup(self):
        for tiles in self.game.tile.values():
            tiles.onclick(tiles.change_color,1)
class main:
    def __init__(self):
        self.tile={}
        self.player=0
        self.created=[]
        self.over=[]
        self.setup()
        self.control=controller(self)
    def setup(self):
        for row in range(3):
            for col in range(3):
                self.tile[(row,col)]=Tile(self, row, col)#aligning tiles in its position
                self.created.append((row,col))

win=Screen()
win.screensize(680,560)
win.colormode(255)#changing turtle screen to accept RBG color code.
win.bgcolor((52,152,219))
main()

win.mainloop()
