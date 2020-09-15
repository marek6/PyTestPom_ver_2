from locators.login_locators import LoginPageLocators
from base.base_page import BasePage


class LoginPage(BasePage):

    def enter_login(self, login):
        self.send_keys(LoginPageLocators.login_input, login)

    def enter_password(self, password):
        self.send_keys(LoginPageLocators.password_input, password)

    def click_login_button(self):
        self.click_element(LoginPageLocators.login_button)

    def is_valid_login(self):
        return self.is_element_visible(LoginPageLocators.valid_login)

    def invalid_login_msg(self):
        return self.is_element_visible(LoginPageLocators.invalid_login_message)

    def login_to_portal(self, login, password):
        self.enter_login(login)
        self.enter_password(password)
        self.click_login_button()
