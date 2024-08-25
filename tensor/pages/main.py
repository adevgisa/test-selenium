from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

#from sbis.pages.main import SbisMainPage

from generic.base_page import BasePage

from tensor.pages.about import TensorAboutPage
 
 
class TensorMainPage(BasePage):

    locators = {
        'block_strength_in_humans': (
            'XPATH',
            "//div[@id='container']//div["
                "p[contains(@class,'tensor_ru-Index__card-title')"
                " and contains(text(), 'Сила в людях')]"
            "]"
        ),
    }

    def go_to_about(self):
        link_about = self.block_strength_in_humans.find_element(
            *(By.CSS_SELECTOR, 'a[href="/about"]')
        )
        self.wait.until(EC.element_to_be_clickable(link_about))
        self.driver.execute_script("arguments[0].click();", link_about)

        return TensorAboutPage(self.driver)
