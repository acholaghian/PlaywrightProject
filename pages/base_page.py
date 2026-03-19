from playwright.sync_api import Page
from config.config import config


# The Base Page object for all pages

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        # Passing the module-level config instance so this class can use its base URL
        self.config = config
    
    def navigate(self, sub_url : str):
        self.page.goto(self.config.base_url + sub_url)