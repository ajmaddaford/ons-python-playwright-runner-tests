from playwright.sync_api import Locator

from base_pages.submit_base_page import SubmitBasePage


class SubmitPage(SubmitBasePage):
    def __init__(self, page):
        super().__init__(page,'submit')

    def name_answer(self) -> Locator:
        return self.page.locator('[data-qa="name-answer"]')

    def name_answer_edit(self) -> Locator:
        return self.page.locator('[data-qa="name-answer-edit"]')
