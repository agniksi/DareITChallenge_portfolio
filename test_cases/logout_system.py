import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard import Dashboard

class TestLogout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://scouts-test.futbolkolektyw.pl/en")

    def tearDown(self):
        self.driver.quit()

    def test_successful_logout(self):
        login_page = LoginPage(self.driver)
        dashboard_page = login_page.login("your_username", "your_password")

        dashboard_page.logout()
        self.assertTrue(login_page.is_login_page_displayed())

if __name__ == "__main__":
    unittest.main()
