from dataclasses import dataclass

from base_pages.base_page import BasePage

@dataclass()
class SubmitBasePage(BasePage):
    def __init__(self, page_name):
        super().__init__(page_name)

    def url(self) -> str:
        return f"/questionnaire/{self.page_name}"

