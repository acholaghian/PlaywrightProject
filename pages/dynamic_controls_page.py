from playwright.sync_api import expect
from pages.base_page import BasePage


# The Dynamic Controls page
class DynamicControlsPage(BasePage):
    page_url = "/dynamic_controls"

    def navigate(self):
        self.open(self.page_url)

    def page_header(self):
        return self.page.get_by_role("heading", name="Dynamic Controls")

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

    # Methods for enabling/disabling elements to be used for test setup.

    def enable_checkbox(self):
        if not self.checkbox().is_visible():
            self.add_button().click()
            not expect(self.checkbox()).to_be_hidden()
        else:
            return

    def disable_checkbox(self):
        if self.checkbox().is_visible():
            self.remove_button().click()
            expect(self.checkbox()).to_be_hidden()
        else:
            return

    def enable_textbox(self):
        if self.textbox().is_disabled():
            self.enable_button().click()
            expect(self.textbox()).to_be_enabled
        else:
            return

    def disable_textbox(self):
        if not self.textbox().is_disabled():
            self.disable_button().click()
            expect(self.textbox()).to_be_disabled
        else:
            return
