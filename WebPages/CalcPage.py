from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Conf.config import TestData
from WebPages.Page import Page


class CalcPage(Page):

    """Locators of Google Calculator Page"""
    SEARCH_FIELD = (By.NAME, "q")
    SEARCH_BUTTON = (By.NAME, "btnK")
    CALC_TEXTBOX = (By.CLASS_NAME, "jlkklc")
    GOOGLE_LOGO = (By.ID, "logo")
    MEMORY_STR = (By.CLASS_NAME, "vUGUtc")
    RESULT_FIELD = (By.CLASS_NAME, "qv3Wpe")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.GOOGLE_URL)

    """Methods of Google Calculator Page"""

    """Method searches for Google Calculator"""
    """and pushes the search button"""
    def do_search(self, search_string):
        self.do_send_key(self.SEARCH_FIELD, TestData.WORD_CALC)
        self.do_click(self.SEARCH_BUTTON)

    """Method makes Google Calculator process math expression"""
    """and returns the result"""
    def do_math(self, search_expression):
        self.do_send_key(self.CALC_TEXTBOX, TestData.CALC_EXPRESSION)
        self.do_send_key(self.CALC_TEXTBOX, Keys.ENTER)
        self.do_send_key(self.CALC_TEXTBOX)
        result_str = self.driver.find_element(self.RESULT_FIELD).text
        return result_str
