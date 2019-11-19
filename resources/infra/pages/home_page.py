from selenium.webdriver.common.by import By

from resources.infra.pages.base_page import BasePage
from resources.infra.pages.login_page import LoginPage
from resources.settings.base_settings import LOGIN_URL, REGISTRATION_URL


class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)


