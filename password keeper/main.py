


from tkinter import *
from tkinter import messagebox
import random
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

import pandas

def add():
    #is_it_ok = messagebox.askyesno(title="confirmation",message=f'websitename : {website_name.get()} \n username : {email_text.get()}\n password : {password_text.get()}')

    if str(website_name.get()) == ""or str(email_text.get())=="" or str(password_text.get())=="":
        messagebox.showerror(title="error",message="You have left something")



    else:
        is_it_ok = messagebox.askyesno(title="confirmation", message=f'websitename : {website_name.get()} \n username : {email_text.get()}\n password : {password_text.get()}')
        if is_it_ok :
            file= open("D:\\first exe file\data","a")
            file.write(f'\n{website_name.get()}            {email_text.get()}                 {password_text.get()}')
            file.close()
            website_name.delete(0,last=100)
            password_text.delete(0,last=100)

def generatepassword():
    password_text.delete(0,END)
    password=[]
    list_symbol=["!","@","^","*",")"]
    list_alpha = ["a","c","x","i"]
    for k in range(4):
        p1 = random.choice(list_symbol)
        p2=random.choice(range(0,9))
        p3=random.choice(list_alpha)
        password.append(p1)
        password.append(str(p2))
        password.append(p3)
    finalpassword = ""
    finalpassword ="".join(password)


    password_text.insert(0,finalpassword)







button1 =Button(text="Generate password",command=generatepassword)
button1.grid(row=3,column=3,columnspan=2)


button2 =Button(text="Add",width=15,command=add)
button2.grid(row=4,column=1)





window.mainloop()
