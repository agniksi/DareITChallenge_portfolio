from selenium.webdriver.common.by import By

class AddPlayerPage:
    def __init__(cls, driver):
        cls.driver = driver

    def get_add_player_title(cls):
        return cls.driver.find_element(By.XPATH, "//h1[text()='Add a Player']")

    def get_player_name_input(cls):
        return cls.driver.find_element(By.ID, "player-name")

    def get_player_age_input(cls):
        return cls.driver.find_element(By.ID, "player-age")

    def get_save_button(cls):
        return cls.driver.find_element(By.XPATH, "//button[text()='Save']")
