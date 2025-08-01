from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    ANSWER_LOCATOR = ("xpath", "//input[@id='answer']")
    x_element_LOCATOR = ("xpath", "//span[@id='input_value']")
    ROBOT_LOCATOR = ("xpath", "//input[@id='robotCheckbox']")
    ROBOT_RULE_LOCATOR = ("xpath", "//input[@id='robotsRule']")
    SUBMIT_LOCATOR = ("xpath", "//button[@type='submit']")

    x_element = browser.find_element(*x_element_LOCATOR)
    x = x_element.text
    y = calc(x)

    browser.find_element(*ANSWER_LOCATOR).send_keys(y)
    browser.find_element(*ROBOT_LOCATOR).click()
    browser.find_element(*ROBOT_RULE_LOCATOR).click()
    browser.find_element(*SUBMIT_LOCATOR).click()





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()