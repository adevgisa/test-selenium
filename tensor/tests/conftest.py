import os
import pytest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

logs_path = "./logs"

if not os.path.exists(logs_path):
    os.mkdir(logs_path)

@pytest.fixture(scope='session')
def driver(request):
    """Set up webdriver fixture."""
    options = webdriver.FirefoxOptions()
    options.binary_location = "/home/user/.opt/firefox/firefox"
    #options.add_argument('--no-sandbox')
    #options.add_argument('--disable-dev-shm-usage')

    service = Service(service_log_path=logs_path)
    #service = Service(executable_path="/home/user/.local/bin/geckodriver")

    driver = webdriver.Firefox(options=options, service=service)
    driver.set_window_size(1920, 1080)
    driver.maximize_window()
    driver.implicitly_wait(8)

    yield driver

    driver.quit()

