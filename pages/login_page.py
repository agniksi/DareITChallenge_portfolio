from pages.base_page import BasePage
#
#
class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()= 'Sign in']"
    login_url = ('https://scouts-test.futbolkolektyw.pl/en')
    expected_title = 'Scouts panel - sign in'
    title_of_box_xpath = "//*[@id='__next']/form/div/div[1]/h5"
    header_of_box = 'Scouts Panel'
    futbol_kolektyw_logo_xpath = '//*[@title="Logo Scouts Panel"]'

    def type_in_email(cls, email):
        cls.field_send_keys(cls.login_field_xpath, email)

    def type_in_password(cls, password):
        cls.field_send_keys(cls.password_field_xpath, password)

    def click_on_the_sign_in_button(cls):
        cls.click_on_the_element(cls.sign_in_button_xpath)

    def title_of_page(cls):
        assert cls.get_page_title(cls.login_url) == cls.expected_title
