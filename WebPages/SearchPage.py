from selenium.webdriver.common.by import By

from Conf.config import TestData
from WebPages.Page import Page


class SearchPage(Page):

    SEARCH_FIELD = (By.NAME, "q")
    SEARCH_BUTTON = (By.NAME, "btnK")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.GOOGLE_URL)

    def do_search(self, search_string):
        self.do_send_key(self.SEARCH_FIELD, TestData.WORD_CALC)
        self.do_click(self.SEARCH_BUTTON)
