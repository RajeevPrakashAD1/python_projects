import selenium
import selenium
import time
path_of_driver = "C:\development\chromedriver.exe"
from selenium import webdriver


user_name = "prakashrajeev805@gmail.com"
password = "1234qwerasdf"
account_to_use = "ricardo.carvalhu"

from work import InstaFollower

bot = InstaFollower(path_of_driver)
bot.login()
bot.findfollower()
bot.follow()
