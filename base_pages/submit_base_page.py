from playwright.sync_api import Locator

from base_pages.base_page import BasePage


class SubmitBasePage(BasePage):
    def __init__(self, page, page_name):
        super().__init__(page, page_name)
