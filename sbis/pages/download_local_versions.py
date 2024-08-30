from selenium.common.exceptions import (StaleElementReferenceException,
    TimeoutException, UnexpectedAlertPresentException, WebDriverException)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

from common.base_page import BasePage

class SbisDownloadLocalVersionsPage(BasePage):
    page_url = "https://sbis.ru/download"

    locators = {
        'tabs_left': (
            'CSS',
            'div.sbis_ru-VerticalTabs div.sbis_ru-VerticalTabs__left'
        ),
        'tabs_right': (
            'CSS',
            'div.sbis_ru-VerticalTabs div.sbis_ru-VerticalTabs__right'
        )
    }

    @BasePage.page_action
    def switch_left_tab(self, tab_name = ""):
        self.tabs_left.visibility_of_element_located()

        loc = (
            By.XPATH,
            "//div[@class='controls-TabButton__caption'"
            f" and contains(text(), '{tab_name}')]"
        )

        tab_button = self.tabs_left.find_element(*loc)
        self.wait.until(EC.visibility_of(tab_button))

        try:
            cur_url = self.driver.current_url
            tab_button.click()
            self.wait.until(EC.url_changes(cur_url))
        except WebDriverException:
            pass

    @BasePage.page_action
    def switch_right_tab(self, tab_name = ""):
        self.tabs_right.visibility_of_element_located()

        self.logger.info(f'Finding tab button {tab_name}')
        loc = (
            By.XPATH,
            "//div[@class='controls-TabControl-tabButtons']"
            "//div[@class='controls-TabButton__caption']"
            f"/span[contains(text(), '{tab_name}')]"
        )

        tab_button = self.tabs_right.find_element(*loc)
        self.wait.until(EC.visibility_of(tab_button))
        self.logger.info(f'Clicking tab button {tab_name}')

        try:
            cur_url = self.driver.current_url
            tab_button.click()
            self.wait.until(EC.url_changes(cur_url))
        except WebDriverException:
            pass


    @BasePage.page_action
    def download_plugins_web_installer_for_windows(self):
        link = self.get_download_plugins_web_installer_for_windows_link()

        try:
            self.driver.set_page_load_timeout(60)
            self.wait.until(EC.element_to_be_clickable(link)).click()
            self.driver.set_page_load_timeout(5)
        except TimeoutException as e:
            self.log_exception(e, message="Exception while downloading")

        return link

    def get_download_plugins_web_installer_for_windows_link(self):
        self.tabs_right.visibility_of_element_located()

        loc = (
            By.CSS_SELECTOR,
            'div.sbis_ru-DownloadNew-loadLink'
            ' a[href*="sbisplugin-setup-web.exe"]'
        )

        link = self.tabs_right.find_element(*loc)

        return self.wait.until(EC.visibility_of(link))

