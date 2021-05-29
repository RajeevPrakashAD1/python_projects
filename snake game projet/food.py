from turtle import Turtle, Screen
import turtle
import time
import random
import sys
score = 0

print("welcome to snake game")
screen = Screen()
screen.bgcolor("black")
screen.title("       SNAKE GAME")
screen.setup(500, 500)
x = [-40, -20, 0]
l = []
p = 3
for i in range(p):
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
            if l[0].distance(food) < 20:
                global score
                score +=1
                refresh()
                break

            if l[0].xcor() > 610 or l[0].xcor()<-610:
                gameover()
            if l[0].ycor() > 610 or l[0].ycor() < -610:
                gameover()
            p = 3
            for i in range(p-1, 0, -1):

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
            if l[0].distance(food) < 20:

                global score
                score += 1
                refresh()
                break
            if l[0].xcor() > 610 or l[0].xcor()<-610:
                gameover()
            if l[0].ycor() > 610 or l[0].ycor() < -610:
                gameover()
            p = 3
            for i in range(p-1, 0, -1):
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
            if l[0].distance(food) < 20:

                global score
                score += 1
                refresh()
                break
            if l[0].xcor() > 610 or l[0].xcor()<-610:
                gameover()
            if l[0].ycor() > 610 or l[0].ycor() < -610:
                gameover()
            p = 3
            for i in range(p-1, 0, -1):
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
            if l[0].distance(food) < 20:

                global score
                score += 1
                refresh()
                break
            if l[0].xcor() > 610 or l[0].xcor()<-610:
                gameover()
            if l[0].ycor() > 610 or l[0].ycor() < -610:
                gameover()
            p = 3
            for i in range(p-1, 0, -1):
                screen.update()
                x = l[i - 1].xcor()
                y = l[i - 1].ycor()
                l[i].penup()
                l[i].goto(x, y)

            l[0].penup()

            l[0].forward(10)







food = Turtle()
food.penup()
xf = random.randint(-200, 200)
yf = random.randint(-200, 200)
food.setpos((xf, yf))
food.shape("circle")
food.color("blue")
food.speed("fastest")
food.shapesize(0.5,0.5)





screen.onkey(snakemoveup, "Up")
screen.onkey(snakemovedown, "Down")
screen.onkey(snakemoveright, "Right")
screen.onkey(snakemoveleft, "Left")
screen.listen()


sd = Turtle()
sd.hideturtle()
sd.color("red")
sd.penup()
sd.goto(0,250)


sd.write(f"scoreboard:{score}",align="center",font=("Aerial",20,"normal"))

def refresh():


    xf = random.randint(-200, 200)
    yf = random.randint(-200, 200)
    food.setpos((xf, yf))
    sd.clear()
    sd.write(f"scoreboard:{score}", align="center", font=("Aerial", 20, "normal"))
def gameover():

    sdd = Turtle()
    sdd.hideturtle()
    sdd.color("red")
    sdd.penup()
    sdd.write(f"game over:{score}", align="center", font=("Aerial", 20, "normal"))
    sys.exit()



p = Screen()
p.exitonclick()
