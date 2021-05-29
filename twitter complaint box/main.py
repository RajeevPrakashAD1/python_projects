import selenium
import time
path_of_driver = "C:\development\chromedriver.exe"
from selenium import webdriver

driver = webdriver.Chrome(executable_path=path_of_driver)
driver.get("https://twitter.com/")
time.sleep(5)
#login_button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]')
login_button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]')
login_button.click()
time.sleep(5)
login_nun = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
login_nun.click()
login_nun.send_keys("prakashrajeev805@gmail.com")
login_password  = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
login_password.click()
login_password.send_keys("1234qwerasdf")
final_login = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span')
final_login.click()