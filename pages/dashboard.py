import time
from lib2to3.pgen2 import driver

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class Dashboard(BasePage):
    futbol_kolektyw_logo_xpath = '//*[@title="Logo Scouts Panel"]'
    expected_title = 'Scouts panel'
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en'
    add_player_button_xpath = "//*[text()='Add player']"
    #wait = WebDriverWait(driver, 10)

    def title_of_page(cls):
        cls.wait_for_element_to_be_clickable(cls.futbol_kolektyw_logo_xpath)
        # time.sleep(5)
        assert cls.get_page_title(cls.dashboard_url) == cls.expected_title

    #def title_of_page(cls):
        #cls.wait_for_element_to_be_clickable=(cls.futbol_kolektyw_logo_xpath)
        #time.sleep(5)
        #assert cls.get_page_title(cls.dashboard_url) == cls.expected_title


#class DashboardPage:
    #pass