from nose.plugins.attrib import attr

from Pages.homepage import HomePage
from Tests.basetest import BaseTestCase


class SearchProductTest(BaseTestCase):
    """This is a simple smoke test for the search functionality."""

    @attr(type='smoke', project='notopstryk')
    def test_search_page_open(self):
        """After entering a search term the search results page should open."""
        homepage = HomePage(self.driver)
        search_results = homepage.search.search_for('harambe')
        search_results.wait_for_load()
        self.assertTrue(search_results.check_page_loaded())

    @attr(type='smoke', project='notopstryk')
    def test_product_count_found(self):
        """After searching for existing items, 30 products should show up."""
        homepage = HomePage(self.driver)
        search_results = homepage.search.search_for('lampa')
        # Here we have to wait for the search results page to load,
        # because count_products() looks for class names that are also present on the home page.
        search_results.wait_for_load()
        self.assertEqual(search_results.count_products(), 30)
