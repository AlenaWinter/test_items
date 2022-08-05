
from selenium.webdriver.common.by import By
link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
import time

def test_find_add_to_card_btn(browser):
    browser.get(link)
    time.sleep(5)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    button.click()
    assert browser.find_element(By.CSS_SELECTOR,'.btn-add-to-basket').is_displayed(), "Кнопка добавления товара в корзину отсутсвует"
    

    # pytest --language=es C:\selenium_course\test_items.py