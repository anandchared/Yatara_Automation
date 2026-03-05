import os
import pytest
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def login(page):
    return LoginPage(page)


def test_login_success(login):

    email = os.getenv("VALID_EMAIL")
    password = os.getenv("VALID_PASSWORD")

    login.open_login_page()
    login.login(email, password)
    login.verify_login_success()

def test_login_invalid_password(login):

    email = os.getenv("INVALID_EMAIL")
    password = os.getenv("INVALID_PASSWORD")

    login.open_login_page()
    login.login(email, password)
    login.verify_login_failed()