
from turtle import Turtle,Screen
import turtle
import time
import random


from snake import Snake
# from food import Fo
from snakee import Snake


import turtle
import time
import random
import sys

print("welcome to snake game")
screen = Screen()
screen.bgcolor("black")
screen.title("       SNAKE GAME")
screen.setup(width=500, height=500)
screen.tracer(0)



snake = Snake()
screen.listen()

screen.onkey(snake.snakemoveup, "Up")
screen.onkey(snake.snakemovedown, "Down")
screen.onkey(snake.snakemoveright, "Right")
screen.onkey(snake.snakemoveleft, "Left")



from scoreboard import Scoreboard
scoreboard = Scoreboard()


from food2 import Food
food = Food()





def gameover():

    sdd = Turtle()
    sdd.hideturtle()
    #
    # if hiscre < scoreboard.score:
    #     hiscre = scoreboard.score
    #

    sdd.color("red")
    sdd.penup()
    sdd.write(f"game over:{scoreboard.score}", align="center", font=("Aerial", 20, "normal"))
    time.sleep(1)
    snake.resset()
    sdd.clear()
    scoreboard.resset()





gameison = True
while gameison:
    t = 0.04
    screen.update()
    time.sleep(t)



    if snake.l[0].distance(food) < 20:


        food.refresh()
        scoreboard.scoreupdate()
        snake.addsnake()


    if snake.l[0].xcor() > 610 or snake.l[0].xcor() < -620:
        gameover()
    if snake.l[0].ycor() > 310 or snake.l[0].ycor() < -310:
        gameover()

    for part in snake.l[1:]:

        if snake.l[0].distance(part)<1:
            gameover()


    snake.move()

screen.exitonclick()












