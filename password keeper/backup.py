


from tkinter import *
window = Tk()
window.title("password keeper")

window.config(padx=20,pady=20)

window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200,highlightthickness=0)
passimage = PhotoImage(file="resisepasslogo.png")
canvas.create_image(100,100,image=passimage)
canvas.grid(row=0,column=1)

website_name = Entry(width=35)
website_name.grid(row=1,column=1,columnspan=2)
website_name.focus()

labelwebsite = Label(text= "Website")
labelwebsite.grid(row=1,column=0)

email_text = Entry(width=35)
email_text.grid(row=2,column=1,columnspan=2)
email_text.insert(0,'prakashrajeev805@gmail.com')

labelemail = Label(text= "Email")
labelemail.grid(row=2,column=0)

password_text = Entry(width=35)
password_text.grid(row=3,column=1)

labelpass = Label(text= "Pasword:")
labelpass.grid(row=3,column=0)
print(website_name)
import pandas
def add():






button1 =Button(text="Generate password")
button1.grid(row=3,column=3,columnspan=2)


button2 =Button(text="Add",width=15,command=add)
button2.grid(row=4,column=1)





window.mainloop()
