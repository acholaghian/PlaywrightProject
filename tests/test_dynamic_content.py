from playwright.sync_api import expect, Page
from pages.dynamic_content_page import DynamicContentPage

# Test cases for the Dynamic Content page


# Verify the number of dynamic text elements
def test_dynamic_text_count(dynamic_content_page: DynamicContentPage, page : Page):
    expected_amount = 3
    expect(dynamic_content_page.dynamic_text()).to_have_count(expected_amount)

# Verify the number of dynamic image elements
def test_dynamic_image_count(dynamic_content_page: DynamicContentPage, page : Page):
    expected_amount = 3
    expect(dynamic_content_page.dynamic_image()).to_have_count(expected_amount)
    