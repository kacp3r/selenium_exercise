from nose.plugins.attrib import attr
from ddt import ddt, data

from Pages.homepage import HomePage
from Tests.basetest import BaseTestCase
from Objects.users import get_user_data


@ddt
class LoginTest(BaseTestCase):
    """This is series of smoke tests for the login functionality."""

    @attr(type='smoke', project='notopstryk')
    def test_login_page_load(self):
        """Log in page should load when 'zaloguj się' is clicked."""
        homepage = HomePage(self.driver)
        login_page = homepage.login.click_login()
        self.assertTrue(login_page.check_page_loaded())

    @attr(type='smoke', project='notopstryk')
    @data(*get_user_data('../Objects/existing_users.csv'))
    def test_login_successful(self, user):
        """After entering correct login data, user should be logged in."""
        homepage = HomePage(self.driver)
        login_page = homepage.login.click_login()
        login_page.log_in(user)
        self.assertTrue(homepage.login.check_logged_in())
        homepage.login.click_logout()

    @attr(type='smoke', project='notopstryk')
    @data(*get_user_data('../Objects/existing_users.csv'))
    def test_logout_successful(self, user):
        """After clicking 'wyloguj', the user should be logged out."""
        homepage = HomePage(self.driver)
        login_page = homepage.login.click_login()
        login_page.log_in(user)
        homepage.login.click_logout()
        self.assertTrue(homepage.login.check_logged_out())

    @attr(type='smoke', project='notopstryk')
    @data(*get_user_data('../Objects/false_users.csv'))
    def test_login_unsuccessful(self, user):
        """After putting in incorrect login data, an error message should appear."""
        homepage = HomePage(self.driver)
        login_page = homepage.login.click_login()
        login_page.log_in(user)
        self.assertTrue(login_page.check_incorrect_data_message())
