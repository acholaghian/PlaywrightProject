from playwright.sync_api import Page
from config.config import config


# The Dynamic Controls page
class DynamicControlsPage:
    def __init__(self, page: Page):
        self.page = page
        # Passing the module-level config instance so this class can use its base URL
        self.config = config
        self.url = config.base_url + "/dynamic_controls"

    def navigate(self):
        self.page.goto(self.url)