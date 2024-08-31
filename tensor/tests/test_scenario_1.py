import pytest
 
from sbis.pages.main import SbisMainPage
 
 
def test_scenario_1(driver):
    sbis_main = SbisMainPage(driver).navigate()
    sbis_contacts = sbis_main.go_to_contacts()
    tensor_main = sbis_contacts.go_to_tensor()

    assert tensor_main.block_strength_in_humans.is_displayed()

    tensor_about = tensor_main.go_to_about()

    assert tensor_about.driver.current_url == tensor_about.page_url

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
