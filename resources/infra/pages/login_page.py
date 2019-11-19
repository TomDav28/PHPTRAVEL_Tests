from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from resources.infra.pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

        self.email_textbox = (By.CSS_SELECTOR, "input[type='email']")
        self.password_textbox = (By.CSS_SELECTOR, "input[type='password']")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.invalid_login_label = (By.CSS_SELECTOR, ".alert")

    def enter_email(self,email):
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def clear_email(self):
        self.driver.find_element(*self.email_textbox).clear()

    def clear_password(self):
        self.driver.find_element(*self.password_textbox).clear()

    def press_login(self):
        self.driver.find_element(*self.login_button).click()

    def login_as(self,login_case):
        self.enter_email(login_case["email"])
        self.enter_password(login_case["password"])
        self.press_login()

    def clear_fields(self):
        self.clear_email()
        self.clear_password()

    def is_email_textbox_dispalyed(self):
        try:
            return self.driver.find_element(*self.email_textbox).is_displayed()
        except NoSuchElementException:
            return False

    def is_password_textbox_dispalyed(self):
        try:
            return self.driver.find_element(*self.password_textbox).is_displayed()
        except NoSuchElementException:
            return False

    def is_login_button_dispalyed(self):
        try:
            return self.driver.find_element(*self.login_button).is_displayed()
        except NoSuchElementException:
            return False

    def is_invalid_login_alert_displayed(self):
        try:
            return self.driver.find_element(*self.invalid_login_label).is_displayed()
        except NoSuchElementException:
            return False

