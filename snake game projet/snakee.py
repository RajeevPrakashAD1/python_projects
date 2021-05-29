
STARTING_POSITION = [(-40,0), (-20,0), (0,0)]
from turtle import Turtle, Screen
class Snake:

    def __init__(self):

        self.l=[]
        self.showsnake()



    def showsnake(self):
        for position in STARTING_POSITION:


            self.createsnake(position)



    def createsnake(self, position):
        tim2 = Turtle()
        tim2.shape("square")
        tim2.goto(position)

        tim2.color("white")
        self.l.append(tim2)



    def addsnake(self):
        self.createsnake(self.l[-1].position())


    def resset(self):
        for segments in self.l:
            segments.goto(1000,1000)
        self.l.clear()
        for position in STARTING_POSITION:

            tim2 = Turtle()
            tim2.shape("square")
            tim2.goto(position)

            tim2.color("white")
            self.l.append(tim2)

    def move(self):


        for i in range(len(self.l)-1, 0, -1):
            x = self.l[i - 1].xcor()
            y = self.l[i - 1].ycor()
            self.l[i].penup()
            self.l[i].goto(x, y)

        self.l[0].penup()
        self.l[0].forward(10)

    def snakemoveright(self):
        if not self.l[0].heading() == 180:
            self.l[0].setheading(0)
            #
            # forwardgoing = True
            # while forwardgoing:
            #
            #     for i in range(2, 0, -1):
            #
            #         x = self.l[i - 1].xcor()
            #         y = self.l[i - 1].ycor()
            #         self.l[i].penup()
            #         self.l[i].goto(x, y)
            #
            #     self.l[0].penup()
            #     self.l[0].forward(10)


    def snakemovedown(self):
        if not self.l[0].heading() == 90:
            self.l[0].setheading(270)
            # movedown = True
            # while movedown:
            #
            #     for i in range(2, 0, -1):
            #
            #         x = self.l[i - 1].xcor()
            #         y = self.l[i - 1].ycor()
            #         self.l[i].penup()
            #         self.l[i].goto(x, y)
            #
            #     self.l[0].penup()
            #
            #     self.l[0].forward(10)

    def snakemoveup(self):
        if not self.l[0].heading() == 270:
            self.l[0].setheading(90)
            # movedown = True
            #
            # while movedown:
            #
            #     for i in range(2, 0, -1):
            #
            #         x = self.l[i - 1].xcor()
            #         y = self.l[i - 1].ycor()
            #         self.l[i].penup()
            #         self.l[i].goto(x, y)
            #
            #     self.l[0].penup()
            #
            #     self.l[0].forward(10)

    def snakemoveleft(self):
        if not self.l[0].heading() == 0:
            self.l[0].setheading(180)
            # movedown = True
            # while movedown:
            #
            #     for i in range(2, 0, -1):
            #
            #         x = self.l[i - 1].xcor()
            #         y = self.l[i - 1].ycor()
            #         self.l[i].penup()
            #         self.l[i].goto(x, y)
            #
            #     self.l[0].penup()
            #
            #     self.l[0].forward(10)










