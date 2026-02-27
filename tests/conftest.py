import pytest
from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from playwright.sync_api import Page


@pytest.fixture
def login_page(page: Page):
    lp = LoginPage(page)
    lp.navigate()
    return lp


# To get to the Secure Page, we need to log in successfully on the Login Page
@pytest.fixture
def secure_page(page: Page):
    sp = SecurePage(page)
    lp = LoginPage(page)
    lp.navigate()
    lp.login()
    return sp
