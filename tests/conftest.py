import pytest
from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from pages.dynamic_content_page import DynamicContentPage
from pages.dynamic_controls_page import DynamicControlsPage
from playwright.sync_api import Page, expect


@pytest.fixture
def login_page(page: Page):
    lp = LoginPage(page)
    lp.navigate()
    expect(page).to_have_url(lp.url)
    return lp


# To get to the Secure Page, we need to log in successfully on the Login Page
@pytest.fixture
def secure_page(page: Page):
    sp = SecurePage(page)
    lp = LoginPage(page)
    lp.navigate()
    expect(page).to_have_url(lp.url)
    lp.login()
    expect(page).to_have_url(sp.url)
    return sp


@pytest.fixture
def dynamic_content_page(page: Page):
    dcp = DynamicContentPage(page)
    dcp.navigate()
    return dcp

@pytest.fixture
def dynamic_controls_page(page: Page):
    dcp = DynamicControlsPage(page)
    dcp.navigate()
    return dcp