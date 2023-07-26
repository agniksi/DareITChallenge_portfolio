import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#chrome_driver_path = 'C:\Users\agnie\Pulpit\QA\DareITChallenge_portfolio\drivers\chromedriver.exe'
#service = Service(chrome_driver_path)
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class Test(unittest.TestCase):

    @classmethod
    def setUp(cls):
        os.chmod(DRIVER_PATH, 0o755)
        service = Service(executable_path=DRIVER_PATH)
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        cls.driver.fullscreen_window()
        cls.driver.implicitly_wait(IMPLICITLY_WAIT)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    def test_print_nice_words(self):
        print("WELL DONE!!!!!!!!!")

class TestMediumPage(unittest.TestCase):

        @classmethod
        def setUp(cls):
            os.chmod(DRIVER_PATH, 0o755)
            service = Service(executable_path=DRIVER_PATH)
            cls.driver = webdriver.Chrome(service=service)
            cls.driver.get('https://medium.com/')
            cls.driver.fullscreen_window()
            cls.driver.implicitly_wait(IMPLICITLY_WAIT)

        def test_check_title(self):
            actual_title = self.get_page_title('<https://medium.com/>;')
            expected_title = "Medium – Where good ideas find you."
            assert actual_title == expected_title


        def get_page_title(self, url):
                return self.driver.title

        @classmethod
        def tearDown(cls):
            cls.driver.quit()

    # Element of the first task: Try to search the Internet yourself how to get rid of the error:
    # "DeprecationWarning: executable_path has been deprecated, please pass in a Service object"
