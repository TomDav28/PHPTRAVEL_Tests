from resources.infra.pages.account_page import AccountPage
from resources.infra.pages.home_page import HomePage
from resources.infra.pages.login_page import LoginPage
from resources.settings.base_settings import HOMEPAGE_URL
from resources.tests.base_tests.base_test import BaseTest


class LoginTests(BaseTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # Go to home page and move to login
        cls.browser.go_to_url(HOMEPAGE_URL)
        homepage = HomePage(cls.driver)
        homepage.go_to_login_page()
        cls.browser.wait_for_url_fraction("login")
        cls.login_page = LoginPage(cls.driver)

    def setUp(self):
        # Given parameters - login case and expected result
        self.should_pass = self.param["should_pass"]
        self.login_case = self.param["login_case"]

        # Assertions
        self.assertTrue(self.login_page.is_email_textbox_dispalyed())
        self.assertTrue(self.login_page.is_password_textbox_dispalyed())
        self.assertTrue(self.login_page.is_login_button_dispalyed())
        self.assertIn("my account", self.login_page.get_my_account_button_text().lower())

    def test_login_case(self):
        # Try to login
        self.login_page.login_as(self.login_case)

        if self.should_pass:
            # If successful - load account page
            self.browser.wait_for_url_fraction("account")
            self.account_page = AccountPage(self.driver)

            # Assertions
            self.assertTrue(self.account_page.is_greeting_displayed())
            self.assertIn("hi, ", self.account_page.get_greeting_text().lower())
            self.assertNotIn("my account", self.account_page.get_my_account_button_text())


        else:
            # Assertions
            self.assertTrue(self.login_page.is_email_textbox_dispalyed())
            self.assertTrue(self.login_page.is_password_textbox_dispalyed())
            self.assertTrue(self.login_page.is_login_button_dispalyed())
            self.assertTrue(self.login_page.is_invalid_login_alert_displayed())

    def tearDown(self):
        # If logged in
        if self.should_pass:
            # Logout - should be redirected to login page
            self.account_page.logout()
            self.browser.wait_for_url_fraction("login")

        # If failed to log in - clear fields
        else:
            self.login_page.clear_fields()
