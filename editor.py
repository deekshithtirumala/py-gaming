from turtle import *
wn=Screen()
wn.colormode(255)
t=Turtle()


t.color(83, 58, 27)
wn.onclick(lambda x,y:t.goto(x,y))
wn.mainloop()
