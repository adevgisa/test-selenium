import os
import pytest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

logs_path = "./logs"

if not os.path.exists(logs_path):
    os.mkdir(logs_path)

tmp_path = "/home/user/tmp"

if not os.path.exists(tmp_path):
    os.mkdir(tmp_path)

os.environ["TMPDIR"] = tmp_path


@pytest.fixture(scope='session')
def driver(request):
    """Set up webdriver fixture."""
    options = Options()
    #options.add_argument('--no-sandbox')
    #options.add_argument('--disable-dev-shm-usage')

    service = Service(service_log_path=logs_path)
    #service = Service(executable_path="/home/user/.local/bin/geckodriver")

    driver = webdriver.Firefox(options=options, service=service)
    driver.set_window_size(1920, 1080)
    driver.maximize_window()
    driver.implicitly_wait(8)

    #driver.get("https:\\sbis.ru")

    yield driver
    driver.quit()

