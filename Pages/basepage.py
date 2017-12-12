class BasePage(object):
    # all pages inherit from this object
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    # this imports the search field, which is present on all pages
    @property
    def search(self):
        from Pages.searchpage import SearchRegion
        return SearchRegion(self.driver)

    # the login region is also present on all pages
    @property
    def login(self):
        from Pages.loginpage import LoginRegion
        return LoginRegion(self.driver)
