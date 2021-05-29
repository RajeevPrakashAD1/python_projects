
RED = "#FF0000"
GREEN = "#00FF00"
YELLOW= "#fff875"
font_name = "Courier"
BLUE ="#bbccdd"
BROWN = "#440022"
work_time = 25
short_break = 5
long_break = 20
reps = 0

from tkinter import *
import winsound

window = Tk()
window.title("TIME REMINDER")
window.minsize(width=300,height=300)
window.config(bg=YELLOW,padx=100,pady=50)
timer = 0
def countdown(count):
    global reps

    count_min = int(count/60)
    count_sec = count%60


    canvas.itemconfig(text1,text=f'{count_min}:{count_sec}')

    if count>0:
        global timer
        timer=window.after(1000,countdown,count-1)

    else:
        winsound.Beep(500, 5000)

        start()
label = Label(text="TIMER",fg=GREEN,bg=YELLOW,font=(font_name,50))
label.grid(row=1,column=1)
# label.config(padx=200,pady=10)

canvas = Canvas(width=300,height=300,bg=YELLOW,highlightthickness=0)

clockimg = PhotoImage(file="dsdh.png")
canvas.create_image(150,80,image=clockimg)
text1 = canvas.create_text(150,80,text="00:00",fill="black",font=(font_name,20))
canvas.grid(row=2,column=1)

def start():
    global reps
    reps += 1


    if reps == 1:
        label.config(text="WORK TIME",fg=GREEN,bg=YELLOW,font=(font_name,25))
        ar = work_time
        countdown(ar * 60)
    if reps == 2:
        label.config(text="BREAK TIME", fg=GREEN, bg=YELLOW, font=(font_name, 25))
        ar = short_break
        countdown(ar * 60)
    if reps==3:
        label.config(text="WORK TIME", fg=GREEN, bg=YELLOW, font=(font_name, 25))
        ar= work_time
        countdown(ar * 60)
    if reps == 4:
        label.config(text="BREAK TIME", fg=GREEN, bg=YELLOW, font=(font_name, 25))
        ar = short_break
        countdown(ar * 60)
    if reps == 5:
        label.config(text="WORK TIME", fg=GREEN, bg=YELLOW, font=(font_name, 25))
        ar = work_time
        countdown(ar * 60)
    if reps == 6:
        label.config(text="BREAK TIME", fg=GREEN, bg=YELLOW, font=(font_name, 25))
        ar = short_break
        countdown(ar * 60)
    if reps == 7:
        label.config(text="WORK TIME", fg=GREEN, bg=YELLOW, font=(font_name, 25))
        ar = work_time
        countdown(ar * 60)
    if reps == 8:
        label.config(text="LONG BREAK TIME", fg=GREEN, bg=YELLOW, font=(font_name, 25))
        ar = long_break
        countdown(ar * 60)


def reset():
    global reps
    global timer
    reps = 0
    window.after_cancel(timer)
    label.config(text="TIMER",fg=GREEN,bg=YELLOW,font=(font_name,50))
    canvas.itemconfig(text1, text=f'00:00')



button = Button(text="START",command=start)
button.grid(row=3,column=0)
button.config(padx=10,pady=10)
button2 = Button(text="RESET",command=reset)
button2.grid(row=3,column=2)
button2.config(padx=10,pady=10)


















window.mainloop()


