import time
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login_sailor(self, email, password):
        email_address = self.driver.find_element(By.XPATH, '//*[@id="login-tab-pane"]/form/div[1]/input')
        email_address.clear()
        email_address.send_keys(email)
        time.sleep(1)

        password_field = self.driver.find_element(By.XPATH, '//*[@id="login-tab-pane"]/form/div[2]/input')
        password_field.clear()
        password_field.send_keys(password)
        time.sleep(2)

        remember_checkbox = self.driver.find_element(By.ID, 'remember')
        remember_checkbox.click()
        time.sleep(2)

        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-tab-pane"]/form/button')
        login_button.click()
        time.sleep(3)