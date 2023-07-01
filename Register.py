from selenium import webdriver
from os.path import exists  ## imported the  exist method
# from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
import time

def regis_ter():
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get("http://localhost:4200/")
    time.sleep(2)
    driver.find_element(By.XPATH,"//body/app-root[1]/app-navbar[1]/nav[1]/div[1]/div[3]/ul[1]/li[2]/a[1]").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//body/app-root[1]/app-ragister[1]/div[1]/div[1]/div[3]/form[1]/div[1]/input[1]").send_keys("Anuj choubey")
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@id='exampleInputEmail1']").send_keys("AnujChoubey111@gmail.com")
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@id='exampleInputPassword1']").send_keys("123456")
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@id='exampleInputConformPassword1']").send_keys("123456")
    time.sleep(3)
    driver.find_element(By.XPATH,"//body/app-root[1]/app-ragister[1]/div[1]/div[1]/div[3]/form[1]/div[5]").click()
    time.sleep(10)
regis_ter()