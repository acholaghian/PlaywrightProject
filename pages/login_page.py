
from playwright.sync_api import Page
from config.config import config

class LoginPage:

    error_banner_text_user = "Your username is invalid!"
    error_banner_text_password = "Your password is invalid!"

    def __init__(self, page : Page):
        self.page = page
        # Passing the module-level config instance so this class can use its base URL and credentials
        self.config = config 

    def navigate(self):
        self.page.goto(self.config.base_url + "/login")
    
    def header(self):
        return self.page.get_by_role("heading", name="Login Page")

    def login_button(self):
        return self.page.get_by_role("button", name="Login")
    
    # The text entry field for the Username.
    def user_entry(self):
        return self.page.get_by_role("textbox", name="Username")
    
    # The text entry field for the Password.
    def password_entry(self):
        return self.page.get_by_role("textbox", name="Password")
    
    # The little banner that gets displayed at the top of the page when incorrect credentials are used.
    # Using the Div ID as locator for reliability, as Codegen only provides a get_by_text()
    def error_banner(self):
        return self.page.locator("#flash")
    
    # Types the provided credentials into the username and password text entry fields.
    def fill_credentials(self, usern, passw):
        self.user_entry().fill(usern)
        self.password_entry().fill(passw)
    
    # Logs in with config-provided credentials, intended for use in fixture to get to Secure Page.
    def login(self):
        self.fill_credentials(config.username, config.password)
        self.login_button().click()