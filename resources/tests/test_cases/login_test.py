
from resources.infra.pages.account_page import AccountPage
from resources.infra.pages.home_page import HomePage
from resources.infra.pages.login_page import LoginPage
from resources.settings.base_settings import HOMEPAGE_URL
from resources.tests.base_tests.base_test import BaseTest


class LoginTests(BaseTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser.go_to_url(HOMEPAGE_URL)
        homepage = HomePage(cls.driver)
        homepage.go_to_login_page()
        cls.browser.wait_for_url_fraction("login")

    def setUp(self):
        self.login_page = LoginPage(self.driver)
        self.assertTrue(self.login_page.is_email_textbox_dispalyed())
        self.assertTrue(self.login_page.is_password_textbox_dispalyed())
        self.assertTrue(self.login_page.is_login_button_dispalyed())
        self.assertIn("my account", self.login_page.get_my_account_button_text().lower())

    def test_login_case(self):
        should_pass = self.param["should-pass"]
        login_case = self.param["login_case"]
        self.login_page.login_as(login_case)
        if should_pass:
            self.browser.wait_for_url_fraction("account")
            account_page = AccountPage(self.driver)
            self.assertTrue(account_page.is_greeting_displayed())
            self.assertIn("hi, ",account_page.get_greeting_text().lower())
            self.assertNotIn("my account",account_page.get_my_account_button_text())
            account_page.logout()
            self.browser.wait_for_url_fraction("login")
            self.assertTrue(self.login_page.is_email_textbox_dispalyed())
            self.assertTrue(self.login_page.is_password_textbox_dispalyed())
            self.assertTrue(self.login_page.is_login_button_dispalyed())
        else:
            self.login_page.get_email_validation_status()
            self.assertTrue(self.login_page.is_email_textbox_dispalyed())
            self.assertTrue(self.login_page.is_password_textbox_dispalyed())
            self.assertTrue(self.login_page.is_login_button_dispalyed())
            self.assertTrue(self.login_page.is_invalid_login_alert_displayed())
            self.login_page.clear_fields()