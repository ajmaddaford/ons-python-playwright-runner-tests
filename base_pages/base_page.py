from playwright.sync_api import Locator


class BasePage:
    def __init__(self, page, page_name):
        self.page = page
        self.page_name: str = page_name

    def submit(self) -> Locator:
        return self.page.locator('[data-qa="btn-submit"]')
