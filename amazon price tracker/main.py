
import requests
from bs4 import BeautifulSoup
import lxml
response = requests.get(url="https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463",
                   headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
                            "Accept_Language":"en-US,en;q=0.9"})

response.raise_for_status()

response_in_text = response.text
# print(response_in_text)
soup = BeautifulSoup(response_in_text,"lxml")
#print(soup.getText)
price = soup.find(name="span", class_="a-size-base a-color-price")
price_in_real_form = price.getText()
list = price_in_real_form.split("$")
actual_price = list[1]
name_li = soup.find(name="span",id="productTitle",class_="a-size-large product-title-word-break")
name = name_li.getText().rstrip().lstrip()


import smtplib
actual_price = float(actual_price)
if actual_price>90:
    print("yaha pahuch gaya")
    my_email = "prakashrajeev115@gmail.com"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user="prakashrajeev115@gmail.com", password="e17pk2110064")
    connection.sendmail(from_addr=my_email,
                        to_addrs="prakashrajeev805@gmail.com", msg=f"subject:hello \n\n {name}\n{actual_price}"
                                                                   f"link {https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463} ")
    connection.close()
