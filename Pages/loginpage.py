from Pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException


class LoginRegion(BasePage):
    '''the login link is present on all pages'''

    # locators
    login_link      = (By.CSS_SELECTOR, 'a.login')
    logout_link     = (By.CSS_SELECTOR, 'a.logout')

    def click_login(self):
        self.driver.find_element(*self.login_link).click()
        return LoginPage(self.driver)

    def click_logout(self):
        self.driver.find_element(*self.logout_link).click()
    # this does not return a page, because it goes back to whatever page you were on before

    def check_logged_in(self):
        try:
            self.driver.find_element(*self.logout_link)
            return True
        except WebDriverException:
            return False

    def check_logged_out(self):
        try:
            self.driver.find_element(*self.login_link)
            return True
        except WebDriverException:
            return False


"""
The problem with the check_logged_in method is that if you try to check for an element that isn't there,
even in a 'try: except:' pattern, the driver throws an exception later when we try to call driver.quit()
This is a known issue with the Firefox Gecko driver AFAIK. That's why I'm adding the check_logged_out method.
"""


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # locators
    log_in_message          = (By.CSS_SELECTOR, '.login-head')
    email_input             = (By.CSS_SELECTOR, '#mail_input_long')
    password_input          = (By.CSS_SELECTOR, '#pass_input_long')
    incorrect_data_message  = (By.CSS_SELECTOR, '.alert-error')

    def check_page_loaded(self):
        if 'Zaloguj' in self.driver.find_element(*self.log_in_message).text:
            return True
        return False

    def check_incorrect_data_message(self):
        if 'Niepoprawne' in self.driver.find_element(*self.incorrect_data_message).text:
            return True
        return False

    def log_in(self, user):
        email_field = self.driver.find_element(*self.email_input)
        email_field.clear()
        email_field.send_keys(user['email'])
        password_field = self.driver.find_element(*self.password_input)
        password_field.clear()
        password_field.send_keys(user['password'])
        password_field.submit()
    # this one does not return a page, because it goes back to whatever page you were on before
