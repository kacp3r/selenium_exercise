from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get('https://notopstryk.pl/pl/searchquery/lampa/1/phot/5?url=lampa')

produkt = driver.find_element(By.XPATH, "//div[@class='product s-grid-3 product-main-wrap']")

print(produkt.text)

driver.quit()

"""
notopstryk.test@gmail.com
notopstry

"""
"""
TODO
xxx Opisz wszystkie metody.
xxx Oddziel lokatory.
XXX Dodaj skrypty to nosetests.
Dodaj ptest.
Dodaj Chrome
"""
#shop_category > div.wrap.rwd > header > div.logo-bar.row.container > form > fieldset > input
