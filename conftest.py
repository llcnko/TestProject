import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def init_chrome(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver = driver
    driver.implicitly_wait(3)
    yield
    driver.quit()
