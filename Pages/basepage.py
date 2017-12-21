
class BasePage(object):
    """All pages inherit from this object."""
    def __init__(self, driver):
        self.driver = driver

#    def find_element(self, *locator):
#        return self.driver.find_element(*locator)

    @property
    def search(self):
        """Imports the search field, which is present on all pages."""
        from Pages.searchpage import SearchRegion
        return SearchRegion(self.driver)

    @property
    def login(self):
        """Imports the login region, which is present on all pages."""
        from Pages.loginpage import LoginRegion
        return LoginRegion(self.driver)
