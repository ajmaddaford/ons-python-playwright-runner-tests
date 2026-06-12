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
        page.locator(NameBlockPage.name_label).click()
        expect(page.locator(NameBlockPage.name)).to_be_focused()

    def test_textfield_has_value_when_returning(self, page: Page, open_questionnaire):
        """
        Given text is entered in the textfield
        When user submits and revisits the textfield
        Then the textfield must contain the text entered previously
        """
        open_questionnaire("test_textfield")

        page.locator(NameBlockPage.name).fill("'Twenty><&Five'")
        page.locator(NameBlockPage.submit).click()
        assert SubmitPage().page_name in page.url
        expect(page.locator(SubmitPage.name_answer)).to_have_text("'Twenty><&Five'")
        page.locator(SubmitPage.name_answer_edit).click()

        expect(page.locator(NameBlockPage.name)).to_have_value("'Twenty><&Five'")