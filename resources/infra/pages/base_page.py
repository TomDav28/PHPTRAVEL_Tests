from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from resources.settings.base_settings import LOGIN_URL, REGISTRATION_URL, LOGOUT_URL


class BasePage:

    def __init__(self,driver):
        self.driver=driver
        self.my_account_button = (By.CSS_SELECTOR, ".dropdown-login a")
        self.my_account_label = (By.CSS_SELECTOR, ".dropdown-login i")
        self.login_button = (By.CSS_SELECTOR,".dropdown-menu a[href='{url}']".format(url=LOGIN_URL))
        self.sign_up_button = (By.CSS_SELECTOR,".dropdown-menu a[href='{url}']".format(url=REGISTRATION_URL))
        self.logout_button = (By.CSS_SELECTOR,".dropdown-menu a[href='{url}']".format(url=LOGOUT_URL))

    def open_my_account_dropdown(self):
        self.driver.find_element(*self.my_account_button).click()

    def is_my_account_button_displayed(self):
        try:
            return self.driver.find_element(*self.my_account_button).is_displayed()
        except NoSuchElementException:
            return False

    def get_my_account_button_text(self):
        return self.driver.find_element(*self.my_account_button).text

    def go_to_login_page(self):
        self.open_my_account_dropdown()
        self.driver.find_element(*self.login_button).click()

    def go_to_registration_page(self):
        self.open_my_account_dropdown()
        self.driver.find_element(*self.sign_up_button).click()