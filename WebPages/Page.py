class Page:

    def __int__(self, driver):
        self.driver = driver

    def fill_in(self, txt, locator, by_what):
        self.driver.find_element(by_what, locator).send_keys(txt)

    def click_on(self, locator, by_what):
        self.driver.implicitly_wait(5)
        self.driver.find_element(by_what, locator).click()

    def extract_text(self, locator, by_what):
        self.driver.implicitly_wait(5)
        el = self.driver.find_element(by_what, locator)
        return el.text
