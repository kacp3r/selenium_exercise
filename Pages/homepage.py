from selenium.webdriver.common.by import By
from Pages.basepage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
