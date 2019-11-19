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
        cls.browser.go_to_url(HOMEPAGE_URL)
        homepage = HomePage(cls.driver)
        homepage.go_to_registration_page()
        cls.browser.wait_for_url_fraction("register")

    def setUp(self):
        self.registration_page = RegistrationPage(self.driver)
        self.assertTrue(self.registration_page.is_email_textbox_dispalyed())
        self.assertTrue(self.registration_page.is_first_name_textbox_dispalyed())
        self.assertTrue(self.registration_page.is_last_name_textbox_dispalyed())
        self.assertTrue(self.registration_page.is_phone_textbox_dispalyed())
        self.assertTrue(self.registration_page.is_password_textbox_dispalyed())
        self.assertTrue(self.registration_page.is_confirm_password_textbox_dispalyed())
        self.assertTrue(self.registration_page.is_sign_up_button_dispalyed())
        self.assertIn("my account", self.registration_page.get_my_account_button_text().lower())

    def test_registration(self):
        should_pass = self.param["should_pass"]
        registration_data = self.param["registration_case"]

        if should_pass:
            registration_data["email"] = str(uuid.uuid1()) + registration_data["email"]

        self.registration_page.fill_registration_data(registration_data)
        self.registration_page.click_sign_up_button()
        if should_pass:
            self.browser.wait_for_url_fraction("account")
            account_page = AccountPage(self.driver)
            self.assertTrue(account_page.is_greeting_displayed())
            self.assertIn("hi, ", account_page.get_greeting_text().lower())
            self.assertNotIn("my account", account_page.get_my_account_button_text())
            account_page.logout()
            self.browser.wait_for_url_fraction("login")
            login_page = LoginPage(self.driver)
            login_page.go_to_registration_page()
            self.browser.wait_for_url_fraction("register")

        else:
            self.assertTrue(self.registration_page.are_all_errors_displayed(registration_data["errors"]))
            self.browser.refresh()
            pass