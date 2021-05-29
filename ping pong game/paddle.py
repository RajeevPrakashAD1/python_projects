from turtle import Screen, Turtle
class Paddle(Turtle):

    def __init__(self, x, y):

        super().__init__()


        self.speed("fastest")
        self.shapesize(stretch_wid=3, stretch_len=1)
        self.penup()
        self.shape("square")
        self.color("white")

        self.goto(x,y)



    def moveup(self):



        self.goto(self.xcor(), self.ycor() + 20)

    def movedown(self):

        self.goto(self.xcor(), self.ycor() - 20)




