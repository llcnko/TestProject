from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from AutoTests.ParentTest import ParentTest
from Conf.config import TestData
from WebPages.CalcPage import CalcPage


class TestCalcPage(ParentTest):

    """SEARCH_FIELD = (By.NAME, "q")
    SEARCH_BUTTON = (By.NAME, "btnK")
    CALC_TEXT_BOX = (By.CLASS_NAME, "jlkklc")"""

    def test_memory_string(self):
        self.calcPage = CalcPage(self.driver)
        self.driver.find_element(CalcPage.SEARCH_FIELD).send_keys(TestData.WORD_CALC)
        self.driver.find_element(CalcPage.SEARCH_BUTTON).click()
        self.driver.find_element(CalcPage.CALC_TEXTBOX).send_keys(TestData.CALC_EXPRESSION)
        self.driver.find_element(CalcPage.SEARCH_FIELD).send_keys(Keys.ENTER)
        # force page up as page scrolls down for some reason
        self.driver.find_element(CalcPage.GOOGLE_LOGO).send_keys(Keys.CONTROL + Keys.HOME)
        mmr_str = self.driver.find_element(CalcPage.MEMORY_STR).text
        assert mmr_str == TestData.CALC_EXPRESSION + " =", 'Memory string IS correct'
        assert 1 == 1, 'Memory string is NOT correct'

    def test_calc_result(self):
        # self.calcPage = CalcPage(self.driver)
        reslt = self.driver.find_element(CalcPage.RESULT_FIELD).text
        assert reslt == TestData.RESULT, 'Result IS equal to zero'
        assert 1 == 1, 'Result is NOT equal to zero'
