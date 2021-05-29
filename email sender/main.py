import smtplib
import  datetime as dt
import pandas
import random
data = open("Quotes.csv.txt","r+")
qotes_text = data.readlines()

final_quates = random.choice(qotes_text)



day_qoutes = dt.datetime(year=2021,month=1,day=4)
day_to_send = day_qoutes.day

if day_to_send == 4:


    my_email = "prakashrajeev115@gmail.com"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user="prakashrajeev115@gmail.com",password="e17pk2110064")
    connection.sendmail(from_addr=my_email,
                        to_addrs="prakashrajeev805@gmail.com",msg=f"subject:hello \n\n {final_quates} ")
    connection.close()

