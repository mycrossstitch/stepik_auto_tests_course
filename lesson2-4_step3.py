from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    BUTTON_LOCATOR=("xpath", "//button[@id='book']")

        # говорим Selenium проверять в течение 12 секунд, пока цена не будет 100$
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element(*BUTTON_LOCATOR).click()

    ANSWER_LOCATOR = ("xpath", "//input[@id='answer']")
    x_element_LOCATOR = ("xpath", "//span[@id='input_value']")
    SUBMIT_LOCATOR = ("xpath", "//button[@type='submit']")
    x_element = browser.find_element(*x_element_LOCATOR)
    x = x_element.text
    y = calc(x)

    browser.find_element(*ANSWER_LOCATOR).send_keys(y)

    browser.find_element(*SUBMIT_LOCATOR).click()






finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()