from selenium.webdriver.common.by import By

from WebPages.Page import Page


class SearchPage(Page):

    SEARCH_FIELD = (By.NAME, "q")
    SEARCH_BUTTON = (By.NAME, "btnK")

    def __int__(self, driver):
        super().__int__(driver)

    def do_search(self, search_string):
        self.do_send_key(self.SEARCH_FIELD, search_string)
        self.do_click(self.SEARCH_BUTTON)
