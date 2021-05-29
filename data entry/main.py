import selenium
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
path_of_driver = "C:\development\chromedriver.exe"
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import lxml

my_form = "https://docs.google.com/forms/d/1fxgzq22mYMWqjq6hCH5MMn369ZUnjCdukBKg0vcGphQ/edit#responses"



link_to_google_form = "https://docs.google.com/forms/d/e/1FAIpQLScW3vv4vijeHcYte_887Y0lIjviUmYuh9bCdLbyK1gjEhsGHw/viewform?usp=sf_link"



# driver.get(link_to_google_form)
# response = requests.get(url='https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.93456332403713%2C%22east%22%3A-122.20671908575588%2C%22south%22%3A37.55894580815514%2C%22north%22%3A38.0396522248877%7D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D',
#                         headers={
#                             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
#                             "Accept_Language": "en-US,en;q=0.9"}
#                         )
# response.raise_for_status()
# response_in_text = response.text
# soup = BeautifulSoup(response_in_text, "lxml")
#
#
#
#
#
#
#
#
#
# prices = []
# price = soup.findAll(name = "div", class_="list-card-price")
# for i in price:
#
#     prices.append(i.getText())
#
#
# address = []
# add = soup.find_all("address",class_='list-card-addr')
# for j in add:
#     address.append(j.getText())
# links = []
# link = soup.findAll("a",class_="list-card-link list-card-link-top-margin list-card-img")
# for i in link:
#     links.append(i.get("href"))
#
# option = webdriver.ChromeOptions()
# option.add_argument("incognito")
driver = webdriver.Chrome(executable_path=path_of_driver)
driver.get(link_to_google_form)
