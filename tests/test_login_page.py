import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
from page.login_page import LoginPage


class LoginTest(unittest.TestCase):

    # Valid Login Test
    def test_valid_login(self):
        baseURL = "https://www.sailor.clothing/login"
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(2)

        lp = LoginPage(driver)
        lp.login_sailor("01746604763", "sailor@123")
        time.sleep(2)
        print('Case 01: Login Successful')
        time.sleep(2)

        driver.close()


    # Invalid Login Test
    def test_Invalid_login(self):
        baseURL = "https://www.sailor.clothing/login"
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(2)

        lp = LoginPage(driver)
        lp.login_sailor("017466047639", "sailor@1234")
        print('Case 02: Invalid Login/User Not Found')
        time.sleep(2)

        driver.close()


    # Empty Fields Test
    def test_empty_fields(self):
        baseURL = "https://www.sailor.clothing/login"
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(3)

        lp = LoginPage(driver)
        lp.login_sailor("", "")
        print('Case 03: Unauthorized')
        time.sleep(2)

        driver.close()