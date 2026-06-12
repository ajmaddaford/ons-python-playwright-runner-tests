from playwright.sync_api import Page, expect
from pages.textfield.name_block import NameBlockPage
from pages.textfield.submit import SubmitPage


class TestTextfield:
    
    def test_click_label_to_focus(self, page: Page, open_questionnaire):
        """
        Given a textfield option,
        A user should be able to click the label of the textfield to focus
        """
        open_questionnaire("test_textfield")
        name_block_page = NameBlockPage(page)
        name_block_page.name_label().click()
        expect(name_block_page.name()).to_be_focused()

    def test_textfield_has_value_when_returning(self, page: Page, open_questionnaire):
        """
        Given text is entered in the textfield
        When user submits and revisits the textfield
        Then the textfield must contain the text entered previously
        """
        open_questionnaire("test_textfield")

        name_block_page = NameBlockPage(page)
        name_block_page.name().fill("'Twenty><&Five'")
        name_block_page.submit().click()

        submit_page = SubmitPage(page)
        assert submit_page.page_name in submit_page.page.url
        expect(submit_page.name_answer()).to_have_text("'Twenty><&Five'")
        submit_page.name_answer_edit().click()

        expect(name_block_page.name()).to_have_value("'Twenty><&Five'")