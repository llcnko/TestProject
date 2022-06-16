from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
#driver = webdriver.Chrome(options=options, executable_path=r'C:/Users/lyubov/PycharmProjects/TestTask/chromedriver.exe')
driver.get("https://www.saucedemo.com/")
input_username = driver.find_element(By.ID, "user-name")
if input_username is None:
   print("Элемент не найден")
else:
   print("Элемент найден")