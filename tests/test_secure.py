from playwright.sync_api import expect, Page
from config.config import config
from pages.secure_page import SecurePage

# Test cases for the Secure Page

# Test case to verify successful logout brings user to Login Page
def test_logout(secure_page : SecurePage, page : Page):
    secure_page.logout_button().click()
    expect(page).to_have_url(config.base_url + "/login") # Verifying by checking the URL