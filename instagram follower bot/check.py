import selenium
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
path_of_driver = "C:\development\chromedriver.exe"
from selenium import webdriver
user_name = "prakashrajeev805@gmail.com"
passwordd = "e17pk2110064"
account_to_use = "ricardo.carvalhu"
driver = webdriver.Chrome(executable_path=path_of_driver)


# driver.get("https://www.instagram.com/accounts/login/")
# time.sleep(2)

driver.get(f'https://www.instagram.com/ricardo.carvalhu/')
time.sleep(2)
login_buttom = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button')
time.sleep(1)
login_buttom.click()
time.sleep(5)

username = driver.find_element_by_name("username")
username.click()
username.send_keys(user_name)
password = driver.find_element_by_name("password")

password.click()
password.send_keys(passwordd)
# login_click = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
# login_click.click()
password.send_keys(Keys.ENTER)
time.sleep(2)
# follow_popup = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
# follow_popup.click()
time.sleep(15)
print("djjhsdfsdfsd")
element = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
# for i in range(10):
#     driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", element)

for i in range(400):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", element)
time.sleep(7)
all_buttons = driver.find_elements_by_css_selector("li button")
for button in all_buttons:
    try:
        print(button)
        button.click()

    except ElementClickInterceptedException:
        cancel_button =driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
        cancel_button.click()
    time.sleep(2)





    # time.sleep(2)