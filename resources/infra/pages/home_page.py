from selenium.webdriver.common.by import By

from resources.infra.pages.base_page import BasePage
from resources.infra.pages.login_page import LoginPage
from resources.settings.base_settings import LOGIN_URL


class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

        self.login_button = (By.CSS_SELECTOR,".dropdown-menu a[href='{url}']".format(url=LOGIN_URL))

    def go_to_login_page(self):
        self.open_my_account_dropdown()
        self.driver.find_element(*self.login_button).click()
