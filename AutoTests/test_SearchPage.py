import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from AutoTests.ParentTest import ParentTest
from Conf.config import TestData
from WebPages import SearchPage


class TestSearchPage(ParentTest):
    @pytest.fixture(scope="class")
    def init_chrome(self, request):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        request.cls.driver = driver
        driver.implicitly_wait(10)
        yield
        driver.close()

    def test_search(self):
        self.searchPage = SearchPage(self.driver)
        self.searchPage.do_search(TestData.WORD_CALC)
