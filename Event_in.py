from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
today_date = datetime.today().strftime('%Y-%m-%d')


def Eve_nts():
    driver = webdriver.Chrome
    # driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get("http://localhost:4200/")
    driver.find_element(By.XPATH, "//input[@id='exampleInputEmail1']").send_keys("anujchoubey918@gmail.com")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='exampleInputPassword1']").send_keys("123456")
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@id='button']").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//a[contains(text(),'Events')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[contains(text(),'Creat Events')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@id='party']").send_keys("Anuj ")
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@id='Place']").send_keys("sagar")
    time.sleep(2)
    presentday = datetime.now()  # or presentday = datetime.today()
    # # Get Yesterday
    # yesterday = presentday - timedelta(1)
    # tomorrow = presentday + timedelta(1)
    # Yesterday =  yesterday.strftime('%d-%m-%Y')
    Today = presentday.strftime('%m-%d-%Y')
    driver.find_element(By.XPATH, "//input[@id='Date']").send_keys(Today)
    time.sleep(2)
    current_time = datetime.now().strftime("%H:%M:%p")
    driver.find_element(By.XPATH,"//input[@id='Time']").send_keys(current_time)
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@id='Hour']").send_keys("1")
    time.sleep(2)
    driver.find_element(By.XPATH,"//textarea[@id='message']").send_keys("aapko jarur aana h ")
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[contains(text(),'Submit')]").click()
    time.sleep(20)

# driver = logi_n()
Eve_nts()
