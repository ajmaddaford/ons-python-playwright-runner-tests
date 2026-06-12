from playwright.sync_api import Page, expect


class TestCensus:
    
    def test_load(self, page: Page, open_questionnaire):
        """
        Given a user tries to launch the census,
        Then it should launch
        """
        open_questionnaire("census_individual_gb_wls")
        locator = page.locator("//h1")
        expect(locator).to_have_text("Coronavirus (COVID-19) and Census 2021")