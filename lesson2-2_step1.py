from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math



try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    NUM1_LOCATOR = ("xpath", "//span[@id='num1']")
    NUM2_LOCATOR = ("xpath", "//span[@id='num2']")
    SELECT_LOCATOR = ("xpath", "//select[@id='dropdown']")
    SUBMIT_LOCATOR = ("xpath", "//button[@type='submit']")


    num1_element = browser.find_element(*NUM1_LOCATOR)
    num2_element = browser.find_element(*NUM2_LOCATOR)
    y = str(int(num1_element.text)+int(num2_element.text))
    print(y)
    select = Select(browser.find_element(*SELECT_LOCATOR))

    select.select_by_value(y)
    browser.find_element(*SUBMIT_LOCATOR).click()





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()