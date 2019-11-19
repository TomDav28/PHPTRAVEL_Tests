from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from resources.infra.pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.first_name_textbox = (By.CSS_SELECTOR, "input[name='firstname']")
        self.last_name_textbox = (By.CSS_SELECTOR, "input[name='lastname']")
        self.phone_textbox = (By.CSS_SELECTOR, "input[name='phone']")
        self.email_textbox = (By.CSS_SELECTOR, "input[name='email']")
        self.password_textbox = (By.CSS_SELECTOR, "input[name='password']")
        self.confirm_password_textbox = (By.CSS_SELECTOR, "input[name='confirmpassword']")
        self.signup_button = (By.CSS_SELECTOR, "button.signupbtn")

        self.first_name_label = (By.XPATH, "//*[text()='The First name field is required.']")
        self.last_name_label = (By.XPATH, "//*[text()='The Last Name field is required.']")
        self.email_label = (By.XPATH, "//*[text()='The Email field is required.']")
        self.invalid_email_label = (
            By.XPATH, "//*[text()='The Email field must contain a valid email address.']")
        self.password_label = (By.XPATH, "//*[text()='The Password field is required.']")
        self.confirm_password_label = (By.XPATH, "//*[text()='The Password field is required.']")
        self.short_password_label = (
            By.XPATH, "//*[text()='The Password field must be at least 6 characters in length.']")
        self.password_mismatch_label = (
            By.XPATH, "//*[text()='Password not matching with confirm password.']")

    def enter_email(self, email):
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def is_email_textbox_dispalyed(self):
        try:
            return self.driver.find_element(*self.email_textbox).is_displayed()
        except NoSuchElementException:
            return False

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.first_name_textbox).send_keys(first_name)

    def is_first_name_textbox_dispalyed(self):
        try:
            return self.driver.find_element(*self.first_name_textbox).is_displayed()
        except NoSuchElementException:
            return False

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name_textbox).send_keys(last_name)

    def is_last_name_textbox_dispalyed(self):
        try:
            return self.driver.find_element(*self.last_name_textbox).is_displayed()
        except NoSuchElementException:
            return False

    def enter_phone(self, phone):
        self.driver.find_element(*self.phone_textbox).send_keys(phone)

    def is_phone_textbox_dispalyed(self):
        try:
            return self.driver.find_element(*self.phone_textbox).is_displayed()
        except NoSuchElementException:
            return False

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def is_password_textbox_dispalyed(self):
        try:
            return self.driver.find_element(*self.password_textbox).is_displayed()
        except NoSuchElementException:
            return False

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(*self.confirm_password_textbox).send_keys(confirm_password)

    def is_confirm_password_textbox_dispalyed(self):
        try:
            return self.driver.find_element(*self.confirm_password_textbox).is_displayed()
        except NoSuchElementException:
            return False

    def is_sign_up_button_dispalyed(self):
        try:
            return self.driver.find_element(*self.signup_button).is_displayed()
        except NoSuchElementException:
            return False

    def fill_registration_data(self, registration_data):
        self.enter_first_name(registration_data["first_name"])
        self.enter_last_name(registration_data["last_name"])
        self.enter_email(registration_data["email"])
        self.enter_phone(registration_data["phone"])
        self.enter_password(registration_data["password"])
        self.enter_confirm_password(registration_data["confirm_password"])

    def click_sign_up_button(self):
        self.driver.find_element(*self.signup_button).click()

    def is_first_name_label_displayed(self):
        try:
            return self.driver.find_element(*self.first_name_label).is_displayed()
        except NoSuchElementException:
            return False

    def is_last_name_label_displayed(self):
        try:
            return self.driver.find_element(*self.last_name_label).is_displayed()
        except NoSuchElementException:
            return False

    def is_email_label_displayed(self):
        try:
            return self.driver.find_element(*self.email_label).is_displayed()
        except NoSuchElementException:
            return False

    def is_invalid_email_label_displayed(self):
        try:
            return self.driver.find_element(*self.invalid_email_label).is_displayed()
        except NoSuchElementException:
            return False

    def is_password_label_displayed(self):
        try:
            return self.driver.find_element(*self.password_label).is_displayed()
        except NoSuchElementException:
            return False

    def is_confirm_password_label_displayed(self):
        try:
            return self.driver.find_element(*self.confirm_password_label).is_displayed()
        except NoSuchElementException:
            return False

    def is_short_password_label_displayed(self):
        try:
            return self.driver.find_element(*self.short_password_label).is_displayed()
        except NoSuchElementException:
            return False

    def is_password_mismatch_label_displayed(self):
        try:
            return self.driver.find_element(*self.password_mismatch_label).is_displayed()
        except NoSuchElementException:
            return False

    def are_all_errors_displayed(self, errors):
        flag_lst = []
        if "first_name" in errors:
            flag_lst.append(self.is_first_name_label_displayed())
        if "last_name" in errors:
            flag_lst.append(self.is_last_name_label_displayed())
        if "short_password" in errors:
            flag_lst.append(self.is_short_password_label_displayed())
        if "password_mismatch" in errors:
            flag_lst.append(self.is_password_mismatch_label_displayed())
        if "password" in errors:
            flag_lst.append(self.is_password_label_displayed())
        if "email" in errors:
            flag_lst.append(self.is_email_textbox_dispalyed())
        if "confirm_password" in errors:
            flag_lst.append(self.is_confirm_password_label_displayed())
        if "invalid_email" in errors:
            flag_lst.append(self.is_invalid_email_label_displayed())
        return all(flag_lst)
