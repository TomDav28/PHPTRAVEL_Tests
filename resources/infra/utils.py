import json
import unittest

from resources.settings.base_settings import LOGIN_CASES_FILE_PATH, TEST_SETTINGS_FILE_PATH, \
    REGISTRATION_CASES_FILE_PATH
from resources.tests.base_tests.param_base_test import ParametrizedTestCase


def get_login_cases():
    with open(LOGIN_CASES_FILE_PATH, encoding="utf8") as f:
        return json.load(f)


def get_registration_cases():
    with open(REGISTRATION_CASES_FILE_PATH, encoding="utf8") as f:
        return json.load(f)


def get_test_suite():
    with open(TEST_SETTINGS_FILE_PATH) as f:
        desired_tests = json.load(f)["tests_to_run"]
    suite = unittest.TestSuite()
    if "login" in desired_tests:
        suite = add_login_to_suite(suite)
    if "register" in desired_tests:
        suite = add_registration_to_suite(suite)
    return suite


def add_login_to_suite(suite):
    from resources.tests.test_cases.login_test import LoginTests

    login_cases = get_login_cases()
    for login_case in login_cases["successful"]:
        suite.addTest(ParametrizedTestCase.parametrize(
            LoginTests,
            param={
                "should_pass": True,
                "login_case": login_case
            }
        ))
    for login_case in login_cases["failing"]:
        suite.addTest(ParametrizedTestCase.parametrize(
            LoginTests,
            param={
                "should_pass": False,
                "login_case": login_case
            }
        ))
    return suite

def add_registration_to_suite(suite):
    from resources.tests.test_cases.registration_test import RegistrationTests

    registration_cases = get_registration_cases()
    for registration_case in registration_cases["successful"]:
        suite.addTest(ParametrizedTestCase.parametrize(
            RegistrationTests,
            param={
                "should_pass": True,
                "registration_case": registration_case
            }
        ))
    for registration_case in registration_cases["failing"]:
        suite.addTest(ParametrizedTestCase.parametrize(
            RegistrationTests,
            param={
                "should_pass": False,
                "registration_case": registration_case
            }
        ))
    return suite



def get_is_headless():
    with open(TEST_SETTINGS_FILE_PATH) as f:
        test_settings = json.load(f)
    return test_settings["is_headless"]
