import platform

from datetime import datetime
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

logs_path = Path("logs")

if not logs_path.exists():
    logs_path.mkdir()
elif not logs_path.is_dir():
    raise Exception(
        f"Failed to make the directory at path {logs_path}:"
        " destination path already exists and it is not a directory"
    )

log_file = Path(f"{datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}.log")

def get_firefox_driver(download_dir = None):
    service = Service(log_path = logs_path)
    #service = Service(executable_path="/home/user/.local/bin/geckodriver")

    options = webdriver.FirefoxOptions()
    #options.add_argument('--no-sandbox')
    #options.add_argument('--disable-dev-shm-usage')

    if platform.uname().system == "Linux":
        ff_bin = Path.home() / ".local" / "bin" / "firefox"
        if ff_bin.is_file():
            options.binary_location = str(ff_bin)

    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.manager.showWhenStarting", False)

    if download_dir is not None:
        options.set_preference("browser.download.dir", str(download_dir))

    options.set_preference("browser.helperApps.neverAsk.saveToDisk",
        "application/x-gzip")

    driver = webdriver.Firefox(options=options, service=service)
    driver.set_window_size(1920, 1080)
    driver.maximize_window()
    driver.implicitly_wait(8)

    return driver

