#import pytest
import os

from selenium import webdriver

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

os.environ["TMPDIR"] = "/home/user/tmp"

options = Options()
#options.add_argument('--no-sandbox')
#options.add_argument('--disable-dev-shm-usage')
#options.add_argument("--profile-root=/home/user/.config/mozilla/tests")

service = Service()
#service = Service(executable_path="/home/user/.local/bin/geckodriver")
driver = webdriver.Firefox(options=options, service=service)
driver.set_window_size(1920, 1080)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('http://selenium.dev/')
