from Pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException


class SearchRegion(BasePage):
    '''the search field is present on all pages'''

    # search field locator
    search_input = (By.CSS_SELECTOR, '.search-input')

    def search_for(self, term):
        search_field = self.driver.find_element(*self.search_input)
        search_field.clear()
        search_field.send_keys(term)
        search_field.submit()
        return SearchResultsPage(self.driver)


class SearchResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # locators
    products_found      = (By.CSS_SELECTOR, '.category-name')
    products_not_found  = (By.CSS_SELECTOR, '.alert-info')

    def check_page_loaded(self):
        # this method checks if the search page has loaded
        try:
            if 'Znaleziono' in self.find_element(*self.products_found).text:
                return True
        except WebDriverException:
            pass
        try:
            if 'Nie znaleziono' in self.find_element(*self.products_not_found).text:
                return True
        except WebDriverException:
            pass
        return False
