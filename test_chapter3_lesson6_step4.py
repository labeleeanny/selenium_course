import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import math
import time


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestParametrize:
    @pytest.mark.parametrize('links', ['236895', '236896', '236897', '236898',
                                                 '236899', '236903', '236904', '236905'])
    def test_text_message(self, browser, links):
        link = f"https://stepik.org/lesson/{links}/step/1"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.implicitly_wait(10)
        input1 = browser.find_element(By.CSS_SELECTOR, "textarea[class]")
        answer = math.log(int(time.time()))
        input1.send_keys(answer)
        button = WebDriverWait(browser, 10).until(
            expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'submit-submission')))
        button.click()
        time.sleep(10)
        message = WebDriverWait(browser, 10).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint')))
        result = message.text
        assert result == 'Correct!', "Срок действия кода истек, попробуйте еще раз"


if __name__ == "__main__":
    pytest.main()
