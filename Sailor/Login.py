from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


# Valid Login Test
class Sailor():
    def test_login_valid(self):
        base_url = 'https://www.sailor.clothing/login'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(base_url)

        # Find Elements
        phone = driver.find_element(By.XPATH, '//*[@id="login-tab-pane"]/form/div[1]/input')
        password = driver.find_element(By.XPATH, '//*[@id="login-tab-pane"]/form/div[2]/input')
        remember = driver.find_element(By. ID, 'remember')
        login_btn = driver.find_element(By.XPATH, '//*[@id="login-tab-pane"]/form/button')

        # Login Action
        phone.clear()
        phone.send_keys('01746604763')
        time.sleep(2)

        password.clear()
        password.send_keys('sailor@123')
        time.sleep(2)

        remember.click()
        time.sleep(2)

        login_btn.click()
        time.sleep(4)
        print('Case 01: Login Successful')

        driver.close()
        time.sleep(1)

    # Invalid Login Test
    def test_login_Invalid(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get("https://www.sailor.clothing/login")

        # Find Elements
        phone = driver.find_element(By.XPATH, '//*[@id="login-tab-pane"]/form/div[1]/input')
        password = driver.find_element(By.XPATH, '//*[@id="login-tab-pane"]/form/div[2]/input')
        remember = driver.find_element(By.ID, 'remember')
        login_btn = driver.find_element(By.XPATH, '//*[@id="login-tab-pane"]/form/button')

        # Login Action
        phone.clear()
        phone.send_keys('017466047639')
        time.sleep(2)

        password.clear()
        password.send_keys('sailor@1234')
        time.sleep(2)

        remember.click()
        time.sleep(2)

        login_btn.click()
        time.sleep(3)
        print('Case 02: Invalid Login/User Not Found')

        driver.close()

    # Empty Fields Test
    def test_empty_fields(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get("https://www.sailor.clothing/login")

        # Find Elements
        phone = driver.find_element(By.XPATH, '//*[@id="login-tab-pane"]/form/div[1]/input')
        password = driver.find_element(By.XPATH, '//*[@id="login-tab-pane"]/form/div[2]/input')
        remember = driver.find_element(By.ID, 'remember')
        login_btn = driver.find_element(By.XPATH, '//*[@id="login-tab-pane"]/form/button')

        # Login Action
        phone.clear()
        phone.send_keys('')
        time.sleep(2)

        password.clear()
        password.send_keys('')
        time.sleep(2)

        remember.click()
        time.sleep(2)

        login_btn.click()
        time.sleep(3)
        print('Case 03: Unauthorized')

        driver.close()


test_obj = Sailor()
test_obj.test_login_valid()
test_obj.test_login_Invalid()
test_obj.test_empty_fields()
