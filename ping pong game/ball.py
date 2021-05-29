
from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.penup()
        self.goto(0,0)
        self.xmove = 10
        self.ymove = 10
    def moveball(self):
        nex_x = self.xcor()+self.xmove
        new_y = self.ycor()+self.ymove
        self.goto(nex_x,new_y)

    def bounce(self):
        self.ymove *= -1

    def paddlebounce(self):

        self.xmove *= -1
    def restart(self):
        self.goto(0,0)
        self.xmove *= -1
        self.ymove *= -1
