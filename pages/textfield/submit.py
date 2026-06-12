from dataclasses import dataclass
from typing import Final

from base_pages.submit_base_page import SubmitBasePage

@dataclass()
class SubmitPage(SubmitBasePage):
    name_answer: Final[str] = '[data-qa="name-answer"]'
    name_answer_edit: Final[str] = '[data-qa="name-answer-edit"]'

    def __init__(self):
        super().__init__('submit')
