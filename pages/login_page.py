from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, '--incorrect url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), f'has no attribute {LOGIN_EMAIL}'
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASS), f'has no attribute {LOGIN_EMAIL}'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), f'has no attribute {REGISTER_EMAIL}'
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASS1), f'has no attribute {REGISTER_PASS1}'
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASS2), f'has no attribute {REGISTER_PASS2}'
