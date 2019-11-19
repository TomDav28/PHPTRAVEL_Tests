from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from resources.infra.pages.base_page import BasePage
from resources.settings.base_settings import LOGOUT_URL


class AccountPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

        self.greeting_label = (By.CSS_SELECTOR,".row h3.text-align-left")

    def logout(self):
        self.open_my_account_dropdown()
        self.driver.find_element(*self.logout_button).click()

    def is_greeting_displayed(self):
        try:
            return self.driver.find_element(*self.greeting_label).is_displayed()
        except NoSuchElementException:
            return False

    def get_greeting_text(self):
        return self.driver.find_element(*self.greeting_label).text

