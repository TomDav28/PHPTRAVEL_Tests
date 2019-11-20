import unittest
from selenium.webdriver.support.wait import WebDriverWait
from resources.infra.browser import BrowserFactory
from resources.settings.base_settings import *
import os
from chai import Chai
import unittest

from resources.tests.base_tests.param_base_test import ParametrizedTestCase


class BaseTest(ParametrizedTestCase):
    @classmethod
    def setUpClass(cls):
        # Create the test scenario's browser and driver objects
        cls.browser = BrowserFactory.create_browser()
        cls.driver = cls.browser.driver

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # Close the browser in the end of the scenario
        cls.browser.driver.quit()