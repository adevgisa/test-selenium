import pytest

from common import config

@pytest.fixture(scope='session')
def driver(request):
    """Set up webdriver fixture."""

    driver = config.get_firefox_driver()

    yield driver

    driver.quit()

