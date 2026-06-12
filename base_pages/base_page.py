from dataclasses import dataclass
from typing import Final


@dataclass()
class BasePage:
    submit: Final[str] = '[data-qa="btn-submit"]'

    def __init__(self, page_name):
        self.page_name = page_name
