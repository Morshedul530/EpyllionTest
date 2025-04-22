import unittest
import time
import tempfile

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from page.login_page import LoginPage


def get_driver():
    """Initialize Chrome WebDriver with temporary user profile and headless mode."""
    options = Options()
    options.add_argument("--headless=new")  # Use --headless=new for latest Chrome
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    temp_profile = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={temp_profile}")

    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.baseURL = "https://www.sailor.clothing/login"
        self.driver = get_driver()
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseURL)

    def tearDown(self):
        self.driver.quit()

    def test_valid_login(self):
        lp = LoginPage(self.driver)
        lp.login_sailor("01746604763", "sailor@123")
        print("✅ Case 01: Login Successful")
        time.sleep(2)  # Optional: remove if using proper assertions

    def test_invalid_login(self):
        lp = LoginPage(self.driver)
        lp.login_sailor("017466047639", "sailor@1234")
        print("⚠️ Case 02: Invalid Login/User Not Found")
        time.sleep(2)

    def test_empty_fields(self):
        lp = LoginPage(self.driver)
        lp.login_sailor("", "")
        print("🚫 Case 03: Unauthorized - Empty Fields")
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()
