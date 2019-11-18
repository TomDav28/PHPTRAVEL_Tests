import unittest
from selenium.webdriver.support.wait import WebDriverWait
from resources.infra.browser import BrowserFactory
from resources.settings.base_settings import *
import os
from chai import Chai

class BaseTest(Chai):
    @classmethod
    def setUpClass(cls):
        cls.browser = BrowserFactory.create_browser()
        cls.driver = cls.browser.driver
        cls.wait = WebDriverWait(cls.driver, 60)

    def setUp(self):
        pass

    def tearDown(self):
        self.browser.driver.close()
        pass

    @classmethod
    def tearDownClass(cls):
        cls.browser.driver.quit()