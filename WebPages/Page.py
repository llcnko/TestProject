from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class Page:

    def __init__(self, driver):
        self.driver = driver

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(by_locator))
        return bool(element)

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(by_locator)).click()

    def do_send_key(self, by_locator, text):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(by_locator)).send_key(text)


