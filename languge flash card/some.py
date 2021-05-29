
from tkinter import *
scree_background_colour = "#363124"
class Quizzgui:

    def __init__(self):
        self.window = Tk()
        self.window.minsize(width=400,height=400)
        self.window.config(padx=0,pady=50,bg=scree_background_colour)
        self.window.title("Quize Time")

        self.canvas = Canvas(width = 250,height=250)
        self.canvas.place(x=75,y=0)


        # self.photo = PhotoImage(file="finalpic.jpg")

        self.button = Button(width =5)
        self.button.place(x=50, y=300)





        self.window.mainloop()
