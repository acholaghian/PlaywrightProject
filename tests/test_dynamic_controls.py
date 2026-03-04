from playwright.sync_api import expect, Page
from pages.dynamic_controls_page import DynamicControlsPage

# Test cases for the Dynamic Controls page

test_text = "Testing text"


# Verify the checkbox can be disabled
def test_disable_checkbox(dynamic_controls_page: DynamicControlsPage, page: Page):
    # First setup test by enabling checkbox
    dynamic_controls_page.enable_checkbox()
    # Now run the test case
    dynamic_controls_page.remove_button().click()
    expect(dynamic_controls_page.checkbox()).to_be_hidden()


# Verify that checkbox can be checked
def test_check_checkbox(dynamic_controls_page: DynamicControlsPage, page: Page):
    # First setup test by enabling checkbox
    dynamic_controls_page.enable_checkbox()
    # Now run test case
    dynamic_controls_page.checkbox().check()
    expect(dynamic_controls_page.checkbox()).to_be_checked()


# Verify the textbox can be enabled
def test_enable_textbox(dynamic_controls_page: DynamicControlsPage, page: Page):
    # First setup test by disabling textbox
    dynamic_controls_page.disable_textbox()
    # Now run the test case
    dynamic_controls_page.enable_button().click()
    expect(dynamic_controls_page.textbox()).to_be_enabled()


# Verify that enabled textbox can have text put in it
def test_fill_textbox(dynamic_controls_page: DynamicControlsPage, page: Page):
    # First setup test by enabling textbox
    dynamic_controls_page.enable_textbox()
    # Now run the test case
    dynamic_controls_page.textbox().fill(test_text)
    expect(dynamic_controls_page.textbox()).to_have_value(test_text)
