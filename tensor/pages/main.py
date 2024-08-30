from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

from common.base_page import BasePage

from tensor.pages.about import TensorAboutPage
 
 
class TensorMainPage(BasePage):
    page_url = "https://tensor.ru"

    locators = {
        'block_strength_in_humans': (
            'XPATH',
            "//div[@id='container']//div["
                "p[contains(@class,'tensor_ru-Index__card-title')"
                " and contains(text(), 'Сила в людях')]"
            "]"
        ),
    }

    @BasePage.page_action
    def go_to_about(self):
        #cookie_agrmt_close = (
        #    By.CSS_SELECTOR,
        #    'div.tensor_ru-CookieAgreement__close'
        #)

        #self.wait.until(EC.element_to_be_clickable(cookie_agrmt_close)).click()

        link_about = self.block_strength_in_humans.find_element(
            *(By.CSS_SELECTOR, 'a[href="/about"]')
        )

        self.wait.until(EC.element_to_be_clickable(link_about))

        #hover_and_click = self.action.move_to_element(link_about).click()
        #hover_and_click.perform()

        self.driver.execute_script(
            "arguments[0].scrollIntoView(); arguments[0].click();",
            link_about
        )

        #link_about.click()

        self.wait.until(EC.url_to_be(TensorAboutPage.page_url))

        return TensorAboutPage(self.driver)
