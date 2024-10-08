import functools
import logging
import time

from pathlib import Path

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
from seleniumpagefactory import PageFactory

from common import config

class BasePage(PageFactory):
    page_url = ""
    _logger = None

    def page_action(action, max_attempts = 10, attempts_pause=1):
        @functools.wraps(action)
        def wrapped_page_action(self, *args, **kwargs):
            for i in range(1, max_attempts + 1):
                try:
                    result = action(self, *args, **kwargs)
                    self.log_action(
                        f"[{i}] try to '{action.__name__}' was success"
                    )

                    return result
                except Exception as e:
                    self.log_exception(e, message=
                        f"[{i}] try to '{action.__name__}'"
                        " was failed due to: "
                    )

                time.sleep(attempts_pause)

            self.log_error(
                f"All attempts to '{action.__name__}' was failed"
            )

        return wrapped_page_action
 
    def __init__(self, driver):
        self.driver = driver
        self.driver.set_page_load_timeout(5)

        self.wait = WebDriverWait(self.driver, 10)

        self.action = ActionChains(self.driver)

        self.logger = BasePage.get_logger()
        

    def find(self, locator):
        return self.driver.find_element(*locator)

    @page_action
    def navigate(self):
        self.driver.get(self.page_url)

        return self

    @classmethod
    def get_logger(cls):
        if cls._logger is not None:
            return cls._logger

        cls._logger = logging.getLogger('selenium')
        cls._logger.propagate = False
        cls._logger.setLevel(logging.INFO)

        handler = logging.FileHandler(Path(config.logs_path, config.log_file))
        formatter = logging.Formatter(
            "%(asctime)s: %(levelname)s: %(name)s: %(message)s"
        )
        handler.setFormatter(formatter)

        cls._logger.addHandler(handler)

        return cls._logger

    def log_action(self, message):
        self.logger.info(self.__class__.__name__ + ': ' + message)

    def log_error(self, message):
        self.logger.error(self.__class__.__name__ + ': ' + message)

    def log_exception(self, exception, message):
        self.logger.error(self.__class__.__name__ 
            + f': {message} {repr(exception)}')
