from selenium.common.exceptions import (StaleElementReferenceException,
    TimeoutException, UnexpectedAlertPresentException)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

from common.base_page import BasePage

from sbis.pages.contacts import SbisContactsPage
from sbis.pages.download_local_versions import SbisDownloadLocalVersionsPage
 
 
class SbisMainPage(BasePage):
    page_url = "https://sbis.ru"

    locators = {
        'link_header_contacts': (
            'CSS',
            'div.sbisru-Header a[href="/contacts"]'
        ),
        'footer': (
            'CSS',
            'div.bodyContent div.sbisru-Footer'
        )
    }

    @BasePage.page_action
    def go_to_contacts(self):
        self.link_header_contacts.element_to_be_clickable()
        self.link_header_contacts.hover()
        self.link_header_contacts.click_button()

        self.wait.until(EC.url_to_be(SbisContactsPage.page_url))

        return SbisContactsPage(self.driver)

    @BasePage.page_action
    def go_to_download_local_versions(self):
        self.footer.visibility_of_element_located()

        loc = (
            By.CSS_SELECTOR,
            'ul.sbisru-Footer__list li.sbisru-Footer__list-item'
            ' a.sbisru-Footer__link[href="/download"]'
        )
        link = self.footer.find_element(*loc)
        self.wait.until(EC.element_to_be_clickable(link))

        self.driver.execute_script(
            "arguments[0].scrollIntoView(); arguments[0].click();",
            link
        )

        self.wait.until(EC.url_to_be(SbisDownloadLocalVersionsPage.page_url))

        return SbisDownloadLocalVersionsPage(self.driver)




