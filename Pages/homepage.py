from Pages.basepage import BasePage


class HomePage(BasePage):
    """This is the object for the home page.
    It has functions because it inherits from BasePage
    Some methods return it.
    """
    def __init__(self, driver):
        super().__init__(driver)
