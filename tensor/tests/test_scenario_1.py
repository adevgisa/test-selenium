import time

import pytest
 
from tensor.pages.about import TensorAboutPage

from sbis.pages.main import SbisMainPage
 
 
def test_scenario_1(driver):
    #driver.get(SbisMainPage.page_url)

    sbis_main = SbisMainPage(driver).navigate()
    sbis_contacts = sbis_main.go_to_contacts()
    tensor_main = sbis_contacts.go_to_tensor()
    tensor_main.driver.close()
    tensor_main.driver.switch_to.window(tensor_main.driver.window_handles[-1])

    assert tensor_main.block_strength_in_humans.is_displayed() == True

    #time.sleep(2)
     
    tensor_about = tensor_main.go_to_about()
    images = tensor_about.get_images_in_block_working()
    img_count = len(images)

    assert img_count > 0

    assert images[0].is_displayed()

    width = images[0].size['width']
    height = images[0].size['height']
    for i in range(1, img_count):
        assert images[i].is_displayed()

        assert images[i].size['width'] == width

        assert images[i].size['height'] == height

        width = images[i].size['width']
        height = images[i].size['height']

    #contacts = driver.find_element(*SbisMainPage.header_contacts)

    # TODO don't forget to uncomment wait until clickable
    #self._wait.until(EC.element_to_be_clickable(contacts))
    #driver.execute_script("arguments[0].click();", contacts)
    #tensor = driver.find_element(*SbisMainPage.contacts_tensor)
    #driver.execute_script("arguments[0].click();", tensor)

    #driver.get("https:\\tensor.ru")
    #elements = driver.find_elements(*TensorAboutPage.strength_in_humans)

    #assert len(elements) == 1

    #about = elements[0].find_element(*TensorAboutPage.about_link)
    #driver.execute_script("arguments[0].click();", about)

    #link = "https://tensor.ru/about"

    #assert about.get_attribute("href") == link

    #driver.get(link)

    #working = driver.find_element(*TensorAboutPage.block_working)

    #images = working.find_elements(*TensorAboutPage.working_images)


    #about_page = TensorAboutPage(driver)

    
 
 
#@pytest.fixture(params=[{"username":"admin", "password":"admin$$"},
                        #{"username":"Admin123", "password":"123"}])
#def get_data(request):
    #return request.param
