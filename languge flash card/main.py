
background_color_ans = "#cc99ff"
from tkinter import *
import  random
import time
screen = Tk()
screen.minsize(height=400,width=500)

screen.config(padx=50,pady=50,bg="#99ffcc")
screen.title("word learning")

screen.grid()



canvas = Canvas(width=400,height=250)
canvas.place(x=0,y=0)
canvas.config(bg="#ffcc99")
word = canvas.create_text(200,125,text="word",font=("aerial",40))
title = canvas.create_text(200,50,text="title",font=("aerial",20))




import pandas
words = pandas.read_csv("language csv.csv")
current_dict=words.to_dict(orient="records")
print(current_dict)

def nextword():

    def flip():
        next_word_eng = next_word["ENGLISH"]
        canvas.itemconfig(title, text="English Meaning")
        canvas.itemconfig(word, text=next_word_eng,font=("aerial",15))
        canvas.config(bg=background_color_ans)
    next_word = random.choice(current_dict )
    next_word_hindi= next_word["HINDI"]
    canvas.itemconfig(title,text="Hindi Word")
    canvas.itemconfig(word,text=next_word_hindi)
    screen.after(3000, flip)








button1=Button(text="YES",width=20,command=nextword)
button1.place(x=0,y=300)
button1.config(bg="#00ff00")
button2=Button(text="NO",width=20,command=nextword)
button2.place(x=250,y=300)
button2.config(bg="#ff0000")


nextword()












screen.mainloop()