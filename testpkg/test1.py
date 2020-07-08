from time import sleep

from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:/Selenium Python/Drivers/chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
driver.maximize_window()
sleep(3)
driver.close()
