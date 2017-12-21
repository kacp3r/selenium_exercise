from selenium.common.exceptions import WebDriverException

from Pages.basepage import BasePage
from Objects.page_elements import LoginRegionElements, LoginPageElements


class LoginRegion(BasePage):
    """The login region at the top is present on all pages."""

    def click_login(self):
        """Clicks the login button."""
        self.driver.find_element(*LoginRegionElements.login_link).click()
        return LoginPage(self.driver)

    def click_logout(self):
        """Clicks the logout button.
        This does not return a page, because it goes back to whatever page you were on before.
        """
        self.driver.find_element(*LoginRegionElements.logout_link).click()

    def check_logged_in(self):
        """Checks if the logout link is present on the page, thus checking if a user has logged in."""
        try:
            self.driver.find_element(*LoginRegionElements.logout_link)
            return True
        except WebDriverException:
            return False

    def check_logged_out(self):
        """ Checks if login link on page, thus if user is NOT logged in.
        I did this, because there was a bug with the Gecko driver throwing an error if it did not find an
        element. This does not occur with older Firefox versions.
        """
        try:
            self.driver.find_element(*LoginRegionElements.login_link)
            return True
        except WebDriverException:
            return False


class LoginPage(BasePage):
    """This is the object for the page where the user logs in."""
    def __init__(self, driver):
        super().__init__(driver)

    def check_page_loaded(self):
        """Looks for a page element appearing only on login page."""
        if 'Zaloguj' in self.driver.find_element(*LoginPageElements.log_in_message).text:
            return True
        return False

    def check_incorrect_data_message(self):
        """Looks for error message on incorrect login data."""
        if 'Niepoprawne' in self.driver.find_element(*LoginPageElements.incorrect_data_message).text:
            return True
        return False

    def log_in(self, user):
        """Logs in with the given user, which is a dict with email and password.
        This one does not return a page, because it goes back to whatever page you were on before.
        """
        email_field = self.driver.find_element(*LoginPageElements.email_input)
        email_field.clear()
        email_field.send_keys(user['email'])
        password_field = self.driver.find_element(*LoginPageElements.password_input)
        password_field.clear()
        password_field.send_keys(user['password'])
        password_field.submit()
