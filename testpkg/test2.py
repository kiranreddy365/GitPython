from time import sleep

from selenium import webdriver

def test01_lunch():
    global driver
    driver = webdriver.Chrome(executable_path='F:/Selenium Python/Drivers/chromedriver.exe')
    driver.maximize_window()
    driver.get("http://newtours.demoaut.com/")

def test02_login():
    driver.find_element_by_xpath("//input[@name='userName']").send_keys("kiran.reddy")
    driver.find_element_by_xpath("//input[@name='password']").send_keys("title@123")
    driver.find_element_by_xpath(("//input[@name='login']")).click()
    sleep(1)
    assert driver.find_element_by_xpath("//*[text()='SIGN-OFF']").is_displayed()

def test03_close():
    driver.close()
