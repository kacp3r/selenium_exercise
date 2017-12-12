from Pages.homepage import HomePage
from Tests.basetest import BaseTestCase


class SearchProductTest(BaseTestCase):
    # test case searching for a product and finding out if the search page opened
    def test_search(self):
        homepage = HomePage(self.driver)
        search_results = homepage.search.search_for('harambe')
        self.assertTrue(search_results.check_page_loaded())
