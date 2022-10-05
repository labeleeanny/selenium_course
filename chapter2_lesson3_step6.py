from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    time.sleep(3)
    button = browser.find_element(By.CLASS_NAME, "trollface")
    button.click()
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, "button[type]")
    button2.click()


finally:
    time.sleep(10)
    browser.quit()
