import pytest
from playwright.sync_api import expect, Page
from pages.dynamic_content_page import DynamicContentPage
from config.config import config

# Test cases for the Dynamic Content page


# Verify the number of dynamic text blocks
def test_dynamic_text_count(dynamic_content_page: DynamicContentPage, page : Page):
    expected_rows = 3
    expect(dynamic_content_page.dynamic_text()).to_have_count(expected_rows)

# Verify the number of dynamic images
def test_dynamic_text_count(dynamic_content_page: DynamicContentPage, page : Page):
    expected_rows = 3
    expect(dynamic_content_page.dynamic_image()).to_have_count(expected_rows)
    