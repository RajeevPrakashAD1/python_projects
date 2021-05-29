
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.color("red")
        self.hideturtle()
        self.goto(x,y)
        self.lscore = 0


        self.write(f'{self.lscore}',align="center",font=("Areial",80,"normal"))

    def update(self):
        self.lscore += 1
        self.clear()
        self.write(f'{self.lscore}', align="center", font=("Areial", 80, "normal"))
