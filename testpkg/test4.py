from time import sleep

from selenium import webdriver
import pytest

class Test_Tests:
    @pytest.fixture()
    def setup(self):
        print("Before method.")
        yield
        print("After method.")

    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(executable_path='F:/Selenium Python/Drivers/chromedriver.exe')
        driver.maximize_window()
        driver.get("http://newtours.demoaut.com/")

    def test01_login(self, setup):
        driver.find_element_by_xpath("//input[@name='userName']").send_keys("kiran.reddy")
        driver.find_element_by_xpath("//input[@name='password']").send_keys("title@123")
        driver.find_element_by_xpath(("//input[@name='login']")).click()
        sleep(1)
        assert driver.find_element_by_xpath("//*[text()='SIGN-OFF']").is_displayed()

    def test02_test2(self, setup):
        print("This is Test02")

    def teardown_class(cls):
        driver.close()
