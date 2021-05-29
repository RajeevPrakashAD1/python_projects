from turtle import Screen,Turtle
from paddle import Paddle
import time
screen = Screen()
screen.setup(width=800, height=600)

screen.bgcolor("black")


from paddle import Paddle
paddle_left = Paddle(-385,0)
paddle_right = Paddle(380,0)
screen.tracer(0)


position = [-300,-200,-100,0,100,200,300]
for j in position:
    line = Paddle(0,j)



from ball import Ball
ball = Ball()



screen.listen()
screen.onkey(paddle_left.moveup, "w")
screen.onkey(paddle_left.movedown, "s")
screen.onkey(paddle_right.moveup, "Up")
screen.onkey(paddle_right.movedown, "Down")
from scoreboard import Scoreboard
leftscoreboard = Scoreboard(-50,200)
rightscoreboard = Scoreboard(50,200)


gameison = True
t=0.1
while gameison:

    screen.update()
    time.sleep(t)
    ball.moveball()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
    if paddle_right.distance(ball) < 50 and ball.xcor()>370 :
        ball.paddlebounce()
    if paddle_left.distance(ball) < 50 and ball.xcor()<-370:
         ball.paddlebounce()
    if ball.xcor()>380 :
        t *= 0.99

        ball.restart()
        leftscoreboard.update()
    if ball.xcor()<-380:
        t *= 0.99
        ball.restart()
        rightscoreboard.update()






screen.exitonclick()


























# screen = Screen()
# screen.setup(width=800,height=600)
#
# screen.bgcolor("black")
#
# screen.tracer(0)
# paddle = Turtle()
# paddle.speed("fastest")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.penup()
# paddle.shape("square")
# paddle.color("white")
#
# paddle.goto(350, 0)
#
#
# screen.listen()
# def moveup():
#
#     paddle.goto(paddle.xcor(), paddle.ycor() + 20)
#
#
#
# def movedown():
#
#     paddle.goto(paddle.xcor(), paddle.ycor() - 20)
#
#
# gameison = True
# while gameison:
#     screen.update()
#     break
#
# screen.onkey(moveup,"Up")
# screen.onkey(movedown,"Down")
#
#
#
#
#
#
#
#
#
# screen.exitonclick()
