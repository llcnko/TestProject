from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from AutoTests.ParentTest import ParentTest
from Conf.config import TestData
from WebPages.CalcPage import CalcPage


class TestCalcPage(ParentTest):

    def test_memory_string(self):
        self.calcPage = CalcPage(self.driver)
        self.driver.find_element(By.NAME, "q").send_keys(TestData.WORD_CALC)
        self.driver.find_element(By.NAME, "btnK").click()
        self.driver.find_element(By.CLASS_NAME, "jlkklc").send_keys(TestData.CALC_EXPRESSION)
        self.driver.find_element(By.CLASS_NAME, "jlkklc").send_keys(Keys.ENTER)
        # force page up as page scrolls down for some reason
        self.driver.find_element(By.ID, "logo").send_keys(Keys.CONTROL + Keys.HOME)
        mmr_str = self.driver.find_element(By.CLASS_NAME, "vUGUtc").text
        assert mmr_str == TestData.CALC_EXPRESSION + " =", 'Memory string is correct'
        assert 1 == 1, 'incorrect'

    def test_calc_result(self):
        # self.calcPage = CalcPage(self.driver)
        reslt = self.driver.find_element(By.CLASS_NAME, "qv3Wpe").text
        assert reslt == TestData.RESULT, 'Result is equal to zero'
        assert 1 == 1, 'incorrect'
