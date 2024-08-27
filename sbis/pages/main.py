from selenium.common.exceptions import (StaleElementReferenceException,
    TimeoutException, UnexpectedAlertPresentException)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

from generic.base_page import BasePage

from sbis.pages.contacts import SbisContactsPage
 
 
class SbisMainPage(BasePage):
    page_url = "https://sbis.ru"

    locators = {
        'link_header_contacts': (
            'CSS',
            'div.sbisru-Header a[href="/contacts"]'
        ),
    }

    @BasePage.page_action
    def go_to_contacts(self):
        self.link_header_contacts.element_to_be_clickable()
        self.link_header_contacts.hover()
        self.link_header_contacts.click_button()

        self.wait.until(EC.url_to_be(SbisContactsPage.page_url))

        return SbisContactsPage(self.driver)
