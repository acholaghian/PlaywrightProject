from playwright.sync_api import Page
from config.config import config

# The Base Page object for all pages


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        # Passing the module-level config instance so this class can use its base URL
        self.config = config
        self.base_url = config.base_url

    def open(self, page_url: str):
        self.page.goto(self.base_url + page_url)
