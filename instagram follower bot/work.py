import selenium
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
path_of_driver = "C:\development\chromedriver.exe"
from selenium import webdriver
user_name = "prakashrajeev805@gmail.com"
passwordd = "e17pk2110064"
account_to_use = "ricardo.carvalhu"

class InstaFollower:

    def __init__(self,path):
        self.driver = webdriver.Chrome(executable_path=path)



    def login(self):

        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        username = self.driver.find_element_by_name("username")
        username.click()
        username.send_keys(user_name)
        password = self.driver.find_element_by_name("password")

        password.click()
        password.send_keys(passwordd)
        # login_click = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
        # login_click.click()
        password.send_keys(Keys.ENTER)

    def findfollower(self):
        time.sleep(5)
        try:
            
            not_now = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
            not_now.click()
            time.sleep(2)
        except:
            pass

        search = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")

        search.send_keys(account_to_use)
        time.sleep(5)
        profile = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[2]/div")
        profile.click()
        time.sleep(4)
        follow_popup = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        follow_popup.click()
        time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()