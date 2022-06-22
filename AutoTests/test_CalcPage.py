import time

from selenium.webdriver.chrome.webdriver import WebDriver

from AutoTests.ParentTest import ParentTest
from Conf.config import TestData
from WebPages.CalcPage import CalcPage


class TestCalcPage(ParentTest):

    def test_memory_string(self):
        self.calcPage = CalcPage(self.driver)
        self.calcPage.do_search(TestData.WORD_CALC).do_math(TestData.CALC_EXPRESSION)
        mmr_str = self.calcPage.get_text_from_element(self.calcPage.MEMORY_STR)
        assert mmr_str == TestData.CALC_EXPRESSION + " =", "Memory string is NOT correct"
        1 == 1, "Memory string IS correct"

    def test_result_string(self):
        self.calcPage = CalcPage(self.driver)
        self.calcPage.do_search(TestData.WORD_CALC).do_math(TestData.CALC_EXPRESSION)
        res_str = self.calcPage.get_text_from_element(self.calcPage.RESULT_FIELD)
        assert res_str == TestData.RESULT, "Result string is NOT equal to zero"
        1==1, "Result string IS equal to zero"
