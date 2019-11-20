import uuid

from resources.infra.pages.account_page import AccountPage
from resources.infra.pages.home_page import HomePage
from resources.infra.pages.login_page import LoginPage
from resources.infra.pages.registration_page import RegistrationPage
from resources.settings.base_settings import HOMEPAGE_URL
from resources.tests.base_tests.base_test import BaseTest


class RegistrationTests(BaseTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # Go to homepage and move to registration page
        cls.browser.go_to_url(HOMEPAGE_URL)
        homepage = HomePage(cls.driver)
        homepage.go_to_registration_page()
        cls.browser.wait_for_url_fraction("register")
        cls.registration_page = RegistrationPage(cls.driver)

    def setUp(self):
        # Given parameters - registration case and expected result
        self.should_pass = self.param["should_pass"]
        self.registration_data = self.param["registration_case"]

        # Assertions
        self.assertTrue(self.registration_page.is_email_textbox_dispalyed())
        self.assertTrue(self.registration_page.is_first_name_textbox_dispalyed())
        self.assertTrue(self.registration_page.is_last_name_textbox_dispalyed())
        self.assertTrue(self.registration_page.is_phone_textbox_dispalyed())
        self.assertTrue(self.registration_page.is_password_textbox_dispalyed())
        self.assertTrue(self.registration_page.is_confirm_password_textbox_dispalyed())
        self.assertTrue(self.registration_page.is_sign_up_button_dispalyed())
        self.assertIn("my account", self.registration_page.get_my_account_button_text().lower())

    def test_registration(self):

        # For a successful registration, a uuid is added to the email address
        if self.should_pass:
            self.registration_data["email"] = str(uuid.uuid1()) + self.registration_data["email"]

        # Try to register with the given data
        self.registration_page.fill_registration_data(self.registration_data)
        self.registration_page.click_sign_up_button()

        # Happy flow - move to account page
        if self.should_pass:
            self.browser.wait_for_url_fraction("account")
            self.account_page = AccountPage(self.driver)

            # Assertions
            self.assertTrue(self.account_page.is_greeting_displayed())
            self.assertIn("hi, ", self.account_page.get_greeting_text().lower())
            self.assertNotIn("my account", self.account_page.get_my_account_button_text())

        # Sad flow - check if relevant errors were given
        else:
            self.assertTrue(self.registration_page.are_all_errors_displayed(self.registration_data["errors"]))

    def tearDown(self):
        # If registered
        if self.should_pass:
            # Logout - should move to login page
            self.account_page.logout()
            self.browser.wait_for_url_fraction("login")
            login_page = LoginPage(self.driver)

            # Move back to registration page
            login_page.go_to_registration_page()
            self.browser.wait_for_url_fraction("register")

        # If not registered
        else:
            # Refresh to clear errors and fields
            self.browser.refresh()
