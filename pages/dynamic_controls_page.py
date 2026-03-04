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
    
    def page_header(self):
        return self.page.get_by_role("heading", name = "Dynamic Controls")
    
    # Remove/Add control section

    def remove_add_header(self):
        return self.page.get_by_role("heading", name="Remove/add")
    
    def checkbox_form(self):
        return self.locator(id="checkbox-example")
    
    def checkbox(self):
        return self.page.get_by_role("checkbox")
    
    def remove_button(self):
        return self.page.get_by_role("button", name="Remove")
    
    def add_button(self):
        return self.page.get_by_role("button", name="Add")
    
    # Enable/disable control section

    def enable_disable_header(self):
        return self.page.get_by_role("heading", name="Enable/disable")
    
    def input_form(self):
        return self.locator(id="input-example")
    
    def textbox(self):
        return self.page.get_by_role("textbox")
    
    def enable_button(self):
        return self.page.get_by_role("button", name="Enable")
    
    def disable_button(self):
        return self.page.get_by_role("button", name="Disable")

    # Loading bar image and text that gets displayed when user clicks to change element

    def loader_bar(self):
        return self.page.locator(id="loading")

    # Confirmation that gets displayed when an element is successfully changed

    def confirmation_message(self, text):
        return self.page.locator(id="message", text=text)
