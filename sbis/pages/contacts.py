import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

from common.base_page import BasePage

from tensor.pages.main import TensorMainPage
 
 
class SbisContactsPage(BasePage):
    page_url = "https://sbis.ru/contacts"

    locators = {
        'link_contacts_tensor':
            ('CSS', 'div#contacts_clients a[href="https://tensor.ru/"]'),

        'link_region_chooser': (
            'CSS',
            'div.sbisru-Contacts div.sbis_ru-container'
            ' span.sbis_ru-Region-Chooser span.sbis_ru-link'
        ),

        'block_partners_list': (
            'XPATH',
            "//div[@id='contacts_list']//div[contains(@data-qa, 'items-container')"
            " and descendant::div[contains(@data-qa, 'item')]]"
        ),

        'dialog_regions_list': (
            'CSS',
            'div[name="dialog"].sbis_ru-Region-Panel'
        )
    }

    @BasePage.page_action
    def go_to_tensor(self):
        self.link_contacts_tensor.element_to_be_clickable()
        self.link_contacts_tensor.click_button()

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[-1])

        return TensorMainPage(self.driver)

    def get_region_chooser_text(self):
        self.link_region_chooser.visibility_of_element_located()

        return self.link_region_chooser.text

    @BasePage.page_action
    def choose_region(self, title):
        self.link_region_chooser.element_to_be_clickable()
        self.link_region_chooser.click_button()

        self.dialog_regions_list.visibility_of_element_located()

        loc = (
            By.CSS_SELECTOR,
            f' li.sbis_ru-Region-Panel__item span.sbis_ru-link[title*="{title}"]'
            ' > span'
        )
        link_region = self.dialog_regions_list.find_element(*loc)
        self.wait.until(EC.visibility_of(link_region))

        cur_url = self.driver.current_url

        hover_and_click = self.action.move_to_element(link_region).click()
        hover_and_click.perform()

        self.wait.until(EC.url_changes(cur_url))


    def get_city_from_partners_list(self):
        self.block_partners_list.visibility_of_element_located()

        loc = (
            By.CSS_SELECTOR,
            'div[data-qa="item"] div.sbisru-Contacts-List__city'
        )

        city = self.block_partners_list.find_element(*loc)

        return self.wait.until(EC.visibility_of(city))

    def get_partners_list(self):
        self.block_partners_list.visibility_of_element_located()

        loc = (
            By.CSS_SELECTOR,
            'div[data-qa="item"] div.sbisru-Contacts-List__item'
            ' div.sbisru-Contacts-List__name'
        )

        partners = self.block_partners_list.find_elements(*loc)
        
        for elem in partners:
            self.wait.until(EC.visibility_of(elem))

        return partners

