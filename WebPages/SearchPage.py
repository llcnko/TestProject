from selenium.webdriver.common.by import By

from WebPages.Page import Page


class SearchPage(Page):

    SEARCH_FIELD = (By.NAME, "q")
    SEARCH_BUTTON = (By.NAME, "btnK")