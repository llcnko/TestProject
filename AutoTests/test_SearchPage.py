import pytest

from AutoTests.ParentTest import ParentTest
from Conf.config import TestData
from WebPages import SearchPage

class TestSearchPage(ParentTest):

    def test_search(self):
        self.searchPage = SearchPage(self.driver)
        self.searchPage.do_search(TestData.WORD_CALC)



