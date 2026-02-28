from playwright.sync_api import Page
from config.config import config


# The Dynamic Content page. Some elements currently WIP.
class DynamicContentPage:
    def __init__(self, page: Page):
        self.page = page
        # Passing the module-level config instance so this class can use its base URL
        self.config = config
        self.url = config.base_url + "/dynamic_content"
    
    def navigate(self):
        self.page.goto(self.url)
    
    def header(self):
        return self.page.get_by_role("heading", name="Dynamic Content")
    
    ## Locator for dynamic images; each one has an index.
    def dynamic_image(self, num):
        return self.page.get_by_role("img")
    
    def dynamic_content_block(self):
        return self.page.locator("#content")

    
    def dynamic_text_row(self):
        return self.page.locator("#content > div row")
    
    def dynamic_text_row_alternate(self):
        return self.dynamic_content_block().locator(".row").locator(".large-10 columns")