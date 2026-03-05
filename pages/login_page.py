import os
from pages.base_page import BasePage
from locators.login_locators import LoginLocators
import time
from playwright.sync_api import expect

base_url = os.getenv("BASE_URL")

class LoginPage(BasePage):

    def open_login_page(self):
        self.open(base_url)

    def login(self, email, password):
        self.page.fill(LoginLocators.EMAIL_INPUT, email)
        self.page.fill(LoginLocators.PASSWORD_INPUT, password)
        self.page.click(LoginLocators.LOGIN_BUTTON)

    def verify_login_success(self):
        self.page.wait_for_url("**/mfa/app/verify")
        assert "/mfa/app/verify" in self.page.url
        self.page.click(LoginLocators.CANCEL_BUTTON)

    def verify_login_failed(self):
        self.page.wait_for_url("**/auth/login")
        assert "/auth/login" in self.page.url
