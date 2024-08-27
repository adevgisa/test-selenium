import functools
import time

import pytest

from utils.location import get_region_name_by_ip
 
from tensor.pages.about import TensorAboutPage

from sbis.pages.main import SbisMainPage
 
 
@pytest.mark.parametrize('rgn_name, rgn_url', [("Камчат", "kamchatskij")])
def test_scenario_2(driver, rgn_name, rgn_url):
#    driver.get(SbisMainPage.page_url)

    sbis_main = SbisMainPage(driver).navigate()
    sbis_contacts = sbis_main.go_to_contacts()
    
    assert sbis_contacts.link_region_chooser.is_displayed()

    #assert sbis_contacts.get_region_chooser_text() == get_region_name_by_ip()

    assert sbis_contacts.block_partners_list.is_displayed()

    sbis_contacts.logger.info('Choosing reginon to ' + rgn_name + ' with url ' + rgn_url)
    sbis_contacts.choose_region(rgn_name)

    assert rgn_name in sbis_contacts.get_region_chooser_text()

    assert rgn_name in sbis_contacts.driver.title

    assert rgn_url in sbis_contacts.driver.current_url

    city = sbis_contacts.get_city_from_partners_list()

    assert city.is_displayed()

    assert rgn_name in city.text

    partners = sbis_contacts.get_partners_list()

    assert len(partners) > 0

    for part in partners:
        assert part.is_displayed()

    assert rgn_name in partners[0].text
