import unittest
from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    # all test cases inherit from this

    def setUp(self):
        # this function is called before every testcase
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        self.driver.get('http://notopstryk.pl')

    def tearDown(self):
        # this is called after every testcase
        self.driver.quit()
