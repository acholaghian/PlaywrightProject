from playwright.sync_api import Page

## Webpage that gets displayed when user successfully logs in on Login Page
class SecurePage:
    def __init__(self, page: Page):
        self.page = page

    def header(self):
        return self.page.get_by_role("heading", name="Secure Area", exact=True)

    # Upon successful login, this page displays a little green banner at the top.
    # Using the Div ID as locator for reliability, as Codegen only provides a get_by_text()
    def success_banner(self):
        return self.page.locator("#flash")
    
    def logout_button(self):
        return self.page.get_by_role("link", name="Logout")