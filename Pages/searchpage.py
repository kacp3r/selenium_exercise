from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.basepage import BasePage
from Objects.page_elements import SearchRegionElements, SearchResultsPageElements


class SearchRegion(BasePage):
    """The search field is present on all pages"""

    def search_for(self, term):
        search_field = self.driver.find_element(*SearchRegionElements.search_input)
        search_field.clear()
        search_field.send_keys(term)
        search_field.submit()
        return SearchResultsPage(self.driver)


class SearchResultsPage(BasePage):
    """This is the page that appears when you search for an item."""
    def __init__(self, driver):
        super().__init__(driver)

    def check_page_loaded(self):
        """Checks for texts that should only appear on the search results page.
        try:
            if 'Znaleziono' in self.driver.find_element(*SearchResultsPageElements.products_found).text:
                return True
        except (WebDriverException, AttributeError):
            pass
        try:
            if 'Nie znaleziono' in self.driver.find_element(*SearchResultsPageElements.products_not_found).text:
                return True
        except (WebDriverException, AttributeError):
            pass
        return False"""
        try:
            if len(self.driver.find_elements(*SearchResultsPageElements.search_filter)) != 0:
                return True
        except WebDriverException:
            pass
        return False

    def count_products(self):
        """Searches the page for product divs, returns their number."""
        try:
            count = self.driver.find_elements(*SearchResultsPageElements.product)
            return len(count)
        except WebDriverException:
            pass
        return 0

    def wait_for_load(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(SearchResultsPageElements.search_filter))
