import selenium

path_of_driver = "C:\development\chromedriver.exe"
from selenium import webdriver
import time

time_end_loop = time.time()+60*1



driver = webdriver.Chrome(executable_path=path_of_driver)

driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element_by_id("cookie")
time_5 = time.time() + 5
while True:


    cookie.click()
    if time.time()>time_5:






        total_money = driver.find_element_by_id("money")
        print(total_money.text)
        total_money=int(total_money.text)

        dic = {}
        #money_buy_cursor = driver.find_element_by_xpath('//*[@id="buyCursor"]/b/text()[2]')
        cursor_click = driver.find_element_by_id("buyCursor")




        money_buy_cursor = driver.find_elements_by_css_selector("#buyCursor b ")

        for i in money_buy_cursor:
            money_required_click = int(i.text.split()[2])
            dic[money_required_click]= cursor_click

        grandma_click = driver.find_element_by_id("buyGrandma")
        money_buy_grandma = driver.find_elements_by_css_selector("#buyGrandma b")
        for i in money_buy_grandma:
            money_required_grandma = int(i.text.split()[2])
            dic[money_required_grandma]= grandma_click

        list_of_moneys = list(dic.keys())
        print(list_of_moneys)
        list_of_moneys_available = []
        for ii in list_of_moneys:
            if ii<total_money:
                list_of_moneys_available.append(ii)
        money_used_to_click = max(list_of_moneys_available)

        print(dic[money_used_to_click])
        to_click =dic[money_used_to_click]
        to_click.click()
        time_5 =time.time()+5

    if time.time()>time_end_loop:
        break
print("hurrah")

