from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait

from common.base_page import BasePage
 
 
class TensorAboutPage(BasePage):
    page_url = 'https://tensor.ru/about'

    locators = {
        'block_working': (
            'XPATH',
            "//div[@id='container']//div[contains(@class, 'tensor_ru-section')"
            " and descendant::h2[contains(text(), 'Работаем')]]"
        ),
    }

    def get_images_in_block_working(self):
        self.block_working.visibility_of_element_located()

        imgs_loc = (
            By.XPATH,
            "//div[@id='container']//div[contains(@class, 'tensor_ru-section')"
            " and descendant::h2[contains(text(), 'Работаем')]]//img"
        )

        #images = self.driver.find_elements(*imgs_loc)

        return self.wait.until(EC.visibility_of_all_elements_located(imgs_loc))

        #imgs_loc = ('css selector', "a div img")
        #images = self.block_working.find_elements(*imgs_loc)
        #for img in images:
        #    self.wait.until(EC.visibility_of(img))

        #return images
