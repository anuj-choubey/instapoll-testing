from selenium import webdriver
from os.path import exists  ## imported the  exist method
# from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
import time
# import driver
def logi_n():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get("http://localhost:4200/")
    driver.find_element(By.XPATH,"//input[@id='exampleInputEmail1']").send_keys("Anujchoubey918@gmail.com")
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@id='exampleInputPassword1']").send_keys("123456")
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[@id='button']").click()
    time.sleep(10)
logi_n()