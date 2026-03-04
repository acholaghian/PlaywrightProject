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
    
    ## Locator for dynamic content block
    
    def dynamic_content_block(self):
        return self.page.locator("#content")

    # Locator for dynamic text section
    def dynamic_text(self):
        return self.page.locator("#content > div.row > div.large-10.columns")
    
    # Locator for dynamic image
    def dynamic_image(self):
        return self.page.locator("#content > div.row > div.large-2.columns")