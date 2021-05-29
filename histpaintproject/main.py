import colorgram


p=colorgram.extract("kkdfk.jpg.jpg",40)
cl=[]
for col in p:
    tt=col.rgb
    r=tt.r
    b=tt.b
    g=tt.g
    myturtle=(r, g, b)


    cl.append(myturtle)
print(cl)
import turtle
from turtle import Turtle
turtle.colormode(255)
turtle.screensize(200,200)
import random
for i in range(20):
    for j in range(10):
        turtle.penup()

        rc=random.choice(cl)
        turtle.dot(20,rc)
        turtle.setpos(-350+j*50,-350+i*50)






pi=turtle.Screen()
pi.exitonclick()