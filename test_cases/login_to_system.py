import os
import unittest
from datetime import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages import login_page
from pages.base_page import BasePage
from pages.dashboard import Dashboard
#chrome_driver_path = 'C:\Users\agnie\Pulpit\QA\DareITChallenge_portfolio\drivers\chromedriver.exe'
#service = Service(chrome_driver_path)
from pages.login_page import LoginPage
from test_cases.add_player_page import AddPlayerPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class DashboardPage:
    pass


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(cls):
        os.chmod(DRIVER_PATH, 0o755)
        service = Service(executable_path=DRIVER_PATH)
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        cls.driver.fullscreen_window()
        cls.driver.implicitly_wait(IMPLICITLY_WAIT)


    @classmethod
    def test_log_in_to_the_system(cls):
        user_login = LoginPage(cls.driver)
        user_login.title_of_page()
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(cls.driver)
        dashboard_page.title_of_page()

    def test_add_a_player_page(cls):
        def test_add_a_player_page(cls):
            user_login = LoginPage(cls.driver)
            user_login.type_in_email('user07@getnada.com')
            user_login.type_in_password('Test-1234')
            user_login.click_on_the_sign_in_button()

            dashboard_page = DashboardPage(cls.driver)
            dashboard_page.click_add_player_button()

            add_player_page = AddPlayerPage(cls.driver)
            assert add_player_page.get_add_player_title().is_displayed()
            assert add_player_page.get_player_name_input().is_displayed()
            assert add_player_page.get_player_age_input().is_displayed()
            assert add_player_page.get_save_button().is_displayed()

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


from pages.dashboard import Dashboard

class TestLogout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://scouts-test.futbolkolektyw.pl/en")

    def tearDown(self):
        self.driver.quit()

    def test_successful_logout(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()

        dashboard_page.logout()
        self.assertTrue(login_page.is_login_page_displayed())

if __name__ == "__main__":
    unittest.main()


