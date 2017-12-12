from Pages.homepage import HomePage
from Tests.basetest import BaseTestCase


class SearchProductTest(BaseTestCase):
    # click 'log in' and check if the login page opened
    def test_login_page_load(self):
        homepage = HomePage(self.driver)
        login_page = homepage.login.click_login()
        self.assertTrue(login_page.check_page_loaded())

    # log in an check if logged in
    def test_login_successful(self):
        user = {'email': 'notopstryk.test@gmail.com', 'password': 'notopstry'}
        homepage = HomePage(self.driver)
        login_page = homepage.login.click_login()
        login_page.log_in(user)
        self.assertTrue(homepage.login.check_logged_in())
        homepage.login.click_logout()

    # log in, log out, check logged out
    def test_logout_successful(self):
        user = {'email': 'notopstryk.test@gmail.com', 'password': 'notopstry'}
        homepage = HomePage(self.driver)
        login_page = homepage.login.click_login()
        login_page.log_in(user)
        homepage.login.click_logout()
        self.assertTrue(homepage.login.check_logged_out())

    def test_login_unsuccessful(self):
        user = {'email': 'fsfasd', 'password': 'fdsafsa'}
        homepage = HomePage(self.driver)
        login_page = homepage.login.click_login()
        login_page.log_in(user)
        self.assertTrue(login_page.check_incorrect_data_message())
