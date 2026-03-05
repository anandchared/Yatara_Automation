import os
from pages.base_page import BasePage
from locators.login_locators import LoginLocators
import time

base_url = os.getenv("BASE_URL")

class LoginPage(BasePage):

    def open_login_page(self):
        self.open(base_url)

    def login(self, email, password):
        self.page.fill(LoginLocators.EMAIL_INPUT, email)
        self.page.fill(LoginLocators.PASSWORD_INPUT, password)
        self.page.click(LoginLocators.LOGIN_BUTTON)

    def verify_login_success(self):
        time.sleep(5)
        assert base_url+"/mfa/app/verify" in self.get_current_url()

    def verify_login_failed(self):
        time.sleep(5)
        assert base_url+"/auth/login" in self.get_current_url()