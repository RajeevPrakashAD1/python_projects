from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()



        xf = random.randint(-350, 350)
        yf = random.randint(-350, 350)
        self.penup()
        self.setpos((xf, yf))
        self.shape("circle")
        self.color("blue")
        self.speed("fastest")
        self.shapesize(0.5, 0.5)
        self.refresh()



    def refresh(self):

        xf = random.randint(-200, 200)
        yf = random.randint(-200, 200)
        self.setpos((xf, yf))

