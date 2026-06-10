import pytest
from playwright.sync_api import Page, expect


class TestTextfield:
    
    def test_click_label_to_focus(self, page: Page, open_questionnaire):
        """
        Given a textfield option,
        A user should be able to click the label of the textfield to focus
        """
        open_questionnaire("test_textfield.json")
        