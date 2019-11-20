import os
import re

from resources.settings.base_settings import CHROMEDRIVER_EXE_PATH, CHROMEDRIVER_DIR_PATH
from resources.settings.run_settings import IS_HEADLESS
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait


class BrowserFactory:
    @staticmethod
    def create_browser(implicitly_wait=10,headless = IS_HEADLESS):
        driver = None
        if headless:
            options = webdriver.ChromeOptions()
            options.add_argument('--no-sandbox')
            options.add_argument('--window-size=1420,1080')
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_experimental_option('w3c', False)
            options.add_argument('--no-proxy-server')
            options.add_argument('--disable-dev-shm-usage')
            if os.name == 'nt':
                driver = webdriver.Chrome(chrome_options=options)
            elif os.name == 'posix':
                driver = webdriver.Chrome(chrome_options=options, executable_path=CHROMEDRIVER_EXE_PATH)
        else:
            if os.name == 'nt':
                driver = webdriver.Chrome()
            elif os.name == 'posix':
                driver = webdriver.Chrome(executable_path=CHROMEDRIVER_EXE_PATH)

        return Browser(driver, implicitly_wait)


class Browser:
    def __init__(self, driver, implicitly_wait=10):
        self.driver = driver
        self.driver.implicitly_wait(implicitly_wait)
        self.wait = WebDriverWait(self.driver, implicitly_wait)

    def go_to_url(self, url):
        self.driver.get(url)

    def current_url(self):
        return self.driver.current_url

    def wait_for_url_fraction(self, url_fraction):
        self.wait.until(lambda driver: re.search(url_fraction, self.current_url()) is not None)

    def add_cookies(self, cookies):
        for cookie in cookies:
            self.add_cookie(cookie)

    def add_cookie(self, cookie):
        self.driver.add_cookie(cookie)

    def drag_and_drop(self, source_element, dest_element):
        ActionChains(self.driver).drag_and_drop(source_element, dest_element).perform()

    def get_active_element(self) -> WebElement:
        return self.driver.switch_to.active_element

    def maximize(self):
        self.driver.maximize_window()

    def minimize(self):
        self.driver.minimize_window()

    def refresh(self):
        self.driver.refresh()