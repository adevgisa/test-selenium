import os
import pytest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

logs_path = "./logs"

if not os.path.exists(logs_path):
    os.mkdir(logs_path)

@pytest.fixture(scope='session')
def tmp_path_download(tmp_path_factory):
    path = tmp_path_factory.mktemp('download')

    yield path

@pytest.fixture(scope='session')
def driver(request, tmp_path_download):
    """Set up webdriver fixture."""
    service = Service(service_log_path=logs_path)
    #service = Service(executable_path="/home/user/.local/bin/geckodriver")

    options = webdriver.FirefoxOptions()
    #options.add_argument('--no-sandbox')
    #options.add_argument('--disable-dev-shm-usage')
    options.binary_location = "/home/user/.opt/firefox/firefox"
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.dir", str(tmp_path_download))
    options.set_preference("browser.helperApps.neverAsk.saveToDisk",
        "application/x-gzip")

    driver = webdriver.Firefox(options=options, service=service)
    driver.set_window_size(1920, 1080)
    driver.maximize_window()
    driver.implicitly_wait(8)

    yield driver

    driver.quit()
