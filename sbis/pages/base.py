from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
 
from seleniumpagefactory import PageFactory
 
class BasePage(PageFactory):
 
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self._driver, 10)
        self.action = ActionChains(self._driver)
 
    def find(self, locator):
        return self.driver.find_element(*locator)
