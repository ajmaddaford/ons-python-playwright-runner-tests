from dataclasses import dataclass
from typing import Final

from base_pages.question_page import QuestionPage

@dataclass()
class NameBlockPage(QuestionPage):
    name: Final[str] = '#name-answer'
    name_label: Final[str] = '[for=name-answer]'

    def __init__(self):
        super().__init__('name-block')