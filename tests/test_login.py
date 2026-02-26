from playwright.sync_api import expect, Page
from pages.login_page import LoginPage
from config.config import config

# Test cases for the Login Page

# Test case to verify the "invalid username" error banner
def test_login_bad_user(login_page: LoginPage):
    account = "wronguser" # We need to use an invalid username instead of the environment credentials.
    login_page.fill_credentials(account, config.password)
    login_page.login_button().click()
    expect(login_page.error_banner()).to_contain_text(login_page.error_banner_text_user)


# Test case to verify the "invalid password" error banner
def test_login_bad_password(login_page: LoginPage):
    password = "wrongpass" # We need to use an invalid password instead of the environment credentials.
    login_page.fill_credentials(config.username, password)
    login_page.login_button().click()
    expect(login_page.error_banner()).to_contain_text(login_page.error_banner_text_password)

# Test case to verify a successful login takes user to Secure Page.
def test_login_success(login_page: LoginPage, page : Page):
    login_page.fill_credentials(config.username, config.password)
    login_page.login_button().click()
    expect(page).to_have_url(config.base_url + "/secure")