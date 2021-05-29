from turtle import Turtle

file = open("highscore.txt","r+")
hiscre = file.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        self.hideturtle()
        self.color("red")
        self.penup()
        file = open("highscore.txt", "r+")
        hsc = int(file.read())
        self.highscore = hsc
        file.close()

        self.goto(0, 250)
        self.speed("fastest")

        self.write(f"scoreboard:{self.score} ****  highscore:{self.highscore}", align="center", font=("Aerial", 20, "normal"))
    def scoreupdate(self):
        self.score  += 1

        self.clear()
        self.write(f"scoreboard:{self.score}  ****    highscore:{self.highscore} ", align="center", font=("Aerial", 20, "normal"))


    def resset(self):
        self.clear()

        file = open("highscore.txt", "r+")
        if self.highscore<self.score:
            self.highscore = self.score



            file.write(f'{self.highscore}')

        self.score = 0

