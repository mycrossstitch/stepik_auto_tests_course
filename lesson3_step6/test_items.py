from selenium.webdriver.common.by import By
import time
link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"



def test_add_to_cart_button_is_present(browser):
    browser.get(link)
    time.sleep(10)  # Проверка языка кнопки вручную
    add_to_cart_button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_to_cart_button, "Add to cart button not found!"