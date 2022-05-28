from lib2to3.pgen2 import driver
from select import select
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

s=Service("chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.find_element_by_xpath("//*[text()='Create New Account']").click()
time.sleep(3)
driver.find_element_by_name("firstname").send_keys("vani")
driver.find_element_by_name("lastname").send_keys("sharma")
time.sleep(2)
driver.find_element_by_name("reg_email__").send_keys("sharma@gmail.com")
driver.find_element_by_name("reg_email_confirmation__").send_keys("sharma@gmail.com")
time.sleep(1)
driver.find_element_by_id("password_step_input").send_keys("9368580279")
day=Select(driver.find_element_by_xpath('//select[@title="Day"]'))
day.select_by_visible_text("24")
month=Select(driver.find_element_by_name("birthday_month"))
month.select_by_visible_text("Sep")
year=Select(driver.find_element_by_name("birthday_year"))
year.select_by_visible_text("2001")
time.sleep(2)
driver.find_element_by_xpath("//label[text()='Female']").click()
driver.find_element_by_xpath("//button[text()='Sign Up']").click()
time.sleep(2)

driver.close()
print("your facebook account is created successfully")