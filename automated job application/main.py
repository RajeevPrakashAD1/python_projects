import selenium
import time
path_of_driver = "C:\development\chromedriver.exe"
from selenium import webdriver

driver = webdriver.Chrome(executable_path=path_of_driver)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2414621052&f_LF=f_AL&geoId=90009624&keywords=python%20developer&location=Greater%20Patna%20Area")

time.sleep(5)
sign_in = driver.find_element_by_class_name("cta-modal__primary-btn")
sign_in.click()

email_input = driver.find_element_by_name("session_key")
email_input.click()
email_input.send_keys("prakashrajeev805@gmail.com")
password_input =  driver.find_element_by_name("session_password")
password_input.send_keys("E17pk2110064@")
time.sleep(5)
sign_in_button = driver.find_element_by_class_name("login__form_action_container ")
sign_in_button.click()



# driver.close()

