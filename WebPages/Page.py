from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class Page:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(by_locator)).click()

    def do_send_key(self, by_locator, text):
        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text_from_element(self, by_locator):
        txt = WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(by_locator)).text
        return txt
