from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self,driver):
        self.driver=driver
        self.my_account_button = (By.CSS_SELECTOR, ".dropdown-login a")
        self.my_account_label = (By.CSS_SELECTOR, ".dropdown-login i")
    def open_my_account_dropdown(self):
        self.driver.find_element(*self.my_account_button).click()

    def is_my_account_button_displayed(self):
        try:
            return self.driver.find_element(*self.my_account_button).is_displayed()
        except NoSuchElementException:
            return False

    def get_my_account_button_text(self):
        return self.driver.find_element(*self.my_account_button).text