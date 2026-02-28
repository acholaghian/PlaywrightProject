import pytest
from playwright.sync_api import expect, Page
from pages.dynamic_content_page import DynamicContentPage
from config.config import config

# Test cases for the Dynamic Content page


# Test case to verify the number of dynamic text blocks
@pytest.mark.skip(reason="WIP")
def test_dynamic_text_count(dynamic_content_page: DynamicContentPage, page : Page):
    expected_rows = 3
    #expect(page.locator("#content").locator(".row").locator(".large-10.colums")).to_have_count(expected_rows)
    expect(dynamic_content_page.dynamic_text_row_alternate()).to_have_count(expected_rows)