import pytest

from common import config

@pytest.fixture(scope='session')
def tmp_download_dir(tmp_path_factory):
    path = tmp_path_factory.mktemp('download')

    yield path

@pytest.fixture(scope='session')
def driver(request, tmp_download_dir):
    """Set up webdriver fixture."""

    driver = config.get_firefox_driver(download_dir = tmp_download_dir)
    
    yield driver

    driver.quit()
