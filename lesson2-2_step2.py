from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
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

    robot_check = browser.find_element(*ROBOT_LOCATOR)
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_check)
    robot_check.click()
    robot_rule = browser.find_element(*ROBOT_RULE_LOCATOR)
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_rule)
    robot_rule.click()

    button = browser.find_element(*SUBMIT_LOCATOR)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()