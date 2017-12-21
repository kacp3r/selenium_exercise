from selenium.webdriver.common.by import By


class LoginRegionElements:
    """Element locators for the login region on all pages."""
    login_link = (By.CSS_SELECTOR, 'a.login')
    logout_link = (By.CSS_SELECTOR, 'a.logout')


class LoginPageElements:
    """Element locators for the login page."""
    log_in_message = (By.CSS_SELECTOR, '.login-head')
    email_input = (By.CSS_SELECTOR, '#mail_input_long')
    password_input = (By.CSS_SELECTOR, '#pass_input_long')
    incorrect_data_message = (By.CSS_SELECTOR, '.alert-error')


class SearchRegionElements:
    """Element locators for the search region on all pages."""
    search_input = (By.CSS_SELECTOR, '.search-input')


class SearchResultsPageElements:
    """Element locators for the search results page."""
    # The two below are texts that only appear on search results pages.
    products_found = (By.CSS_SELECTOR, '.category-name')
    products_not_found = (By.CSS_SELECTOR, '.alert-info')
    # The item below finds the first product div or all of them.
    product = (By.XPATH, "//div[@class='product s-grid-3 product-main-wrap']")
    # The item below is the div with search filters, should only be on search results page
    search_filter = (By.CSS_SELECTOR, '#box_filter')
