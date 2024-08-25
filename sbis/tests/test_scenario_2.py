import time

import pytest

from utils.location import get_region_name_by_ip
 
from tensor.pages.about import TensorAboutPage

from sbis.pages.main import SbisMainPage
 
 
def test_scenario_2(driver):
    driver.get(SbisMainPage.page_url)

    sbis_main = SbisMainPage(driver)
    sbis_contacts = sbis_main.go_to_contacts()
    
    assert sbis_contacts.link_region_chooser.is_displayed() == True

    #assert sbis_contacts.get_region_chooser_text() == get_region_name_by_ip()

    assert sbis_contacts.block_partners_list.is_displayed() == True

    rgn = "Камчат"
    sbis_contacts.choose_region(rgn)

    assert (rgn in sbis_contacts.get_region_chooser_text()) == True

    assert (rgn in sbis_contacts.driver.title) == True

    assert ("kamchatskij" in sbis_contacts.driver.current_url) == True

    city = sbis_contacts.get_city_from_partners_list()

    assert city.is_displayed() == True

    assert (rgn in city.text) == True

    partners = sbis_contacts.get_partners_list()

    assert len(partners) > 0

    for part in partners:
        assert part.is_displayed() == True

    assert (rgn in partners[0].text) == True

    #time.sleep(3)
 
#@pytest.fixture(params=[{"username":"admin", "password":"admin$$"},
                        #{"username":"Admin123", "password":"123"}])
#def get_data(request):
    #return request.param
