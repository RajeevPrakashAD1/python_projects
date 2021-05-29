import pandas
import turtle
screen = turtle.Screen()

screen.title("map game")
screen.addshape("summ.gif")

turtle.shape("summ.gif")


screen.setup(width = 1.0, height = 1.0)

  #remove close,minimaze,maximaze buttons:
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)


cssvdata = pandas.read_csv("mapdata.csv")

coord = cssvdata["coordinates"]
name = cssvdata["States Name"]
list_of_cord  = coord.to_list()
list_of_name = name.to_list()
#print(list_of_name)

# for _ in range(28):
#
#     new_tu = turtle.Turtle()
#     ans = turtle.textinput("guess the state", "next state name")
#     if ans in list_of_name:
#
#         new_tu.penup()
#         new_tu.goto(cssvdata["coordinates"]==ans)
#         new_tu.write(ans,align="center")
#



screen.exitonclick()



