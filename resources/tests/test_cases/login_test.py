
from resources.infra.pages.account_page import AccountPage
from resources.infra.pages.home_page import HomePage
from resources.infra.pages.login_page import LoginPage
from resources.infra.utils import get_login_cases
from resources.settings.base_settings import HOMEPAGE_URL
from resources.tests.base_tests.base_test import BaseTest


class LoginTests(BaseTest):
    def setUp(self):
        self.login_cases = get_login_cases()
        self.browser.go_to_url(HOMEPAGE_URL)
        homepage = HomePage(self.driver)
        homepage.go_to_login_page()
        self.browser.wait_for_url_fraction("login")

    def test_login_page(self):
        login_page = LoginPage(self.driver)
        self.assertTrue(login_page.is_email_textbox_dispalyed())
        self.assertTrue(login_page.is_password_textbox_dispalyed())
        self.assertTrue(login_page.is_login_button_dispalyed())
        self.assertIn("my account", login_page.get_my_account_button_text().lower())

        for login_case in self.login_cases["successful"]:
            login_page.login_as(login_case)
            self.browser.wait_for_url_fraction("account")
            account_page = AccountPage(self.driver)
            self.assertTrue(account_page.is_greeting_displayed())
            self.assertIn("hi, ",account_page.get_greeting_text().lower())
            self.assertNotIn("my account",account_page.get_my_account_button_text())
            account_page.logout()
            self.browser.wait_for_url_fraction("login")
            self.assertTrue(login_page.is_email_textbox_dispalyed())
            self.assertTrue(login_page.is_password_textbox_dispalyed())
            self.assertTrue(login_page.is_login_button_dispalyed())

        for login_case in self.login_cases["failing"]:
            login_page.login_as(login_case)
            self.assertTrue(login_page.is_email_textbox_dispalyed())
            self.assertTrue(login_page.is_password_textbox_dispalyed())
            self.assertTrue(login_page.is_login_button_dispalyed())
            self.assertTrue(login_page.is_invalid_login_alert_displayed())
            login_page.clear_fields()