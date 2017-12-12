from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get('https://notopstryk.pl')


def find_element(*locator):
    return driver.find_element(*locator)


mylocator = (By.CSS_SELECTOR, 'aaa')


try:
    driver.find_element(*mylocator)
    print('yes')
except WebDriverException:
    print('no')

driver.quit()

"""
notopstryk.test@gmail.com
notopstry

"""