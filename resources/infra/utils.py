import json
import unittest

from resources.settings.base_settings import LOGIN_CASES_FILE_PATH, TEST_SETTINGS_FILE_PATH
from resources.tests.base_tests.param_base_test import ParametrizedTestCase


def get_login_cases():
    with open(LOGIN_CASES_FILE_PATH) as f:
        return json.load(f)


def get_test_suite():
    with open(TEST_SETTINGS_FILE_PATH) as f:
        desired_tests = json.load(f)["tests_to_run"]
    suite = unittest.TestSuite()
    if "login" in desired_tests:
        suite = add_login_to_suite(suite)
    return suite


def add_login_to_suite(suite):
    from resources.tests.test_cases.login_test import LoginTests

    login_cases = get_login_cases()
    for login_case in login_cases["successful"]:
        suite.addTest(ParametrizedTestCase.parametrize(
            LoginTests,
            param={
                "should-pass": True,
                "login_case": login_case
            }
        ))
    for login_case in login_cases["failing"]:
        suite.addTest(ParametrizedTestCase.parametrize(
            LoginTests,
            param={
                "should-pass": False,
                "login_case": login_case
            }
        ))
    return suite

def get_is_headless():
    with open(TEST_SETTINGS_FILE_PATH) as f:
        test_settings = json.load(f)
    return test_settings["is_headless"]
