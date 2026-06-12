from dataclasses import dataclass

from base_pages.base_page import BasePage

@dataclass()
class QuestionPage(BasePage):
    def __init__(self, page_name):
        super().__init__(page_name)
