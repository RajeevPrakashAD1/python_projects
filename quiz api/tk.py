
from tkinter import *
scree_background_colour = "#363124"
from brainquizz import Brainquizz
import time


RED = "#FF0000"
GREEN = "#00FF00"
YELLOW= "#fff875"
font_name = "Courier"
BLUE ="#bbccdd"
BROWN = "#440022"
class Quizzgui:

    def __init__(self,quize_clas:Brainquizz):
        self.quize = quize_clas
        self.window = Tk()
        self.window.minsize(width=400,height=400)
        self.window.config(padx=0,pady=0,bg=scree_background_colour)
        self.window.title("Quize Time")

        self.canvas = Canvas(width = 250,height=250,bg="white")
        self.text1 = self.canvas.create_text(125,125,text="Questions",width=230,fill="black",font=(font_name,10))
        self.canvas.place(x=75,y=30)
        self.label = Label(text=f"Score:",fg=GREEN,bg=scree_background_colour,font=(font_name,10))
        self.label.place(x=280,y=0)
        self.get_next_question_to_display()


        false_image = PhotoImage(file="crosspic40.png")
        self.button1 = Button(image=false_image,command=self.iftrue)
        self.button1.place(x=50, y=300)
        self.button1.config(pady=30)

        true_image = PhotoImage(file="tickpic40.png")
        self.button2 = Button(image = true_image,highlightthickness=0,command=self.iffalse)
        self.button2.config(pady=30)
        self.button2.place(x=300, y=300)




        self.window.mainloop()

    def get_next_question_to_display(self):
        self.canvas.config(bg = "white")
        self.label.config(text = f'Score:{self.quize.score}')
        next_qus = self.quize.nextquestion()[0]
        if next_qus == "false":
            self.canvas.itemconfig(self.text1, text=f'Your Final Score : {self.quize.score} \nPlay Again \nThankyou')
            self.button1.config(state="disabled")
            self.button2.config(state = "disabled")

        else:

            self.canvas.itemconfig(self.text1, text=next_qus)
    def iftrue(self):
        self.feedback(self.quize.check("True"))

    def iffalse(self):
        self.feedback(self.quize.check("False"))
    def feedback(self,isright):
        if isright == True:
            self.canvas.config(bg=GREEN)
            self.window.after(1000,self.get_next_question_to_display)

            # self.canvas.config(bg="white")
        else:
            self.canvas.config(bg=RED)
            self.window.after(1000, self.get_next_question_to_display)



