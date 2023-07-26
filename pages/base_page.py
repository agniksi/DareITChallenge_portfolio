import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.settings import DEFAULT_LOCATOR_TYPE
class BasePage():

    def __init__(cls, driver: WebDriver):
        cls.driver = driver

    def field_send_keys(cls, selector, value, locator_type=By.XPATH):
        return cls.driver.find_element(locator_type, selector).send_keys(value)

    def click_on_the_element(cls, selector, selector_type=By.XPATH):
        return cls.driver.find_element(selector_type, selector).click()

    def get_page_title(self, url):
        return self.driver.title

    def wait_for_element_to_be_clickable(cls, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(cls.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        time.sleep(3)

