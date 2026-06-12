from playwright.sync_api import Locator

from base_pages.question_page import QuestionPage


class NameBlockPage(QuestionPage):
    def __init__(self, page):
        super().__init__(page, 'name-block')

    def name(self) -> Locator:
        return self.page.locator('#name-answer')

    def name_label(self) -> Locator:
        return self.page.locator('[for=name-answer]')
