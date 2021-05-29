class Snake():

    def move():
        from turtle import Turtle, Screen
        import turtle
        import time
        import random
        import sys
        print("welcome to snake game")
        screen = Screen()
        screen.bgcolor("black")
        screen.title("       SNAKE GAME")
        screen.setup(500, 500)
        x = [-40, -20, 0]
        l = []
        for i in range(3):
            tim2 = Turtle()
            tim2.shape("square")
            tim2.goto(x[i], 0)

            tim2.color("white")
            l.append(tim2)

        def snakemoveright():
            if not l[0].heading() == 180:
                l[0].setheading(0)
                forwardgoing = True

                while forwardgoing:

                    for i in range(2, 0, -1):

                        x = l[i - 1].xcor()
                        y = l[i - 1].ycor()
                        l[i].penup()
                        l[i].goto(x, y)

                    l[0].penup()
                    l[0].forward(10)

        def snakemovedown():
            if not l[0].heading() == 90:
                l[0].setheading(270)
                movedown = True
                while movedown:

                    for i in range(2, 0, -1):
                        screen.update()
                        x = l[i - 1].xcor()
                        y = l[i - 1].ycor()
                        l[i].penup()
                        l[i].goto(x, y)

                    l[0].penup()

                    l[0].forward(10)

        def snakemoveup():
            if not l[0].heading() == 270:
                l[0].setheading(90)
                movedown = True
                while movedown:

                    for i in range(2, 0, -1):
                        screen.update()
                        x = l[i - 1].xcor()
                        y = l[i - 1].ycor()
                        l[i].penup()
                        l[i].goto(x, y)

                    l[0].penup()

                    l[0].forward(10)

        def snakemoveleft():
            if not l[0].heading() == 0:
                l[0].setheading(180)
                movedown = True
                while movedown:

                    for i in range(2, 0, -1):

                        x = l[i - 1].xcor()
                        y = l[i - 1].ycor()
                        l[i].penup()
                        l[i].goto(x, y)

                    l[0].penup()

                    l[0].forward(10)


        def foood():
            food = Turtle()
            food.penup()
            xf = random.randint(-200, 200)
            yf = random.randint(-200, 200)
            food.setpos((xf, yf))
            food.shape("Circle")
            food.color("blue")
            return xf





        screen.onkey(snakemoveup, "Up")
        screen.onkey(snakemovedown, "Down")
        screen.onkey(snakemoveright, "Right")
        screen.onkey(snakemoveleft, "Left")
        screen.listen()





        p = Screen()
        p.exitonclick()
