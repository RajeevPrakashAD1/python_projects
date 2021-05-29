from turtle import Turtle,Screen
import turtle


screen = Screen()
screen.setup(width=500,height=400)
userinput = screen.textinput("welcome to turtle race bet on your turtle","type a color in small alphabet:")

import random

l = ["red","blue","black","orange","yellow","green"]

ydistace = [-150,-100,-50,0,50,100]
allturtle =[]


for i in range(6):

    newt = Turtle()
    newt.shape("turtle")
    newt.color(l[i])
    newt.penup()
    newt.goto(-230, ydistace[i])


    allturtle.append(newt)
print(allturtle)
if userinput:
    israceon = True
while israceon:

    for turtlee in allturtle:
        if turtlee.xcor() > 230:
            israceon = False
            wit = turtlee.pencolor()
            winingcolor =  wit
            if winingcolor == userinput:
                print("you win")
            else:
                print(f"youloss,{winingcolor} win")
        else:

            turtlee.forward(random.randint(1,20))


p = Screen()
p.exitonclick()

















