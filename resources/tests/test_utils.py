import json
import unittest
from resources.settings.base_settings import LOGIN_CASES_FILE_PATH, TEST_SETTINGS_FILE_PATH, \
    REGISTRATION_CASES_FILE_PATH, FLIGHT_CASES_FILE_PATH
from resources.tests.base_tests.param_base_test import ParametrizedTestCase

'''
        Extract the provided test cases
'''


def get_login_cases():
    with open(LOGIN_CASES_FILE_PATH, encoding="utf8") as f:
        return json.load(f)


def get_flight_cases():
    with open(FLIGHT_CASES_FILE_PATH) as f:
        return json.load(f)


def get_registration_cases():
    with open(REGISTRATION_CASES_FILE_PATH, encoding="utf8") as f:
        return json.load(f)


'''
        Add the provided scenarios to the test suite
'''


def add_login_to_suite(suite):
    from resources.tests.test_cases.login_test import LoginTests

    login_cases = get_login_cases()

    # For each provided test case - create a parametrized test case and add to suite
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

    # For each provided test case - create a parametrized test case and add to suite
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


def add_flight_to_suite(suite):
    from resources.tests.test_cases.flight_test import FlightTests

    flight_cases = get_flight_cases()

    # For each provided test case - create a parametrized test case and add to suite
    for flight_case in flight_cases["cases"]:
        suite.addTest(ParametrizedTestCase.parametrize(
            FlightTests,
            param={
                "flight_case": flight_case
            }
        ))
    return suite


# Extract the provided headless settings
def get_is_headless():
    with open(TEST_SETTINGS_FILE_PATH) as f:
        test_settings = json.load(f)
    return test_settings["is_headless"]

# Aggregate all test into one suite
def get_test_suite():
    # Get the scenarios provided
    with open(TEST_SETTINGS_FILE_PATH) as f:
        desired_tests = json.load(f)["tests_to_run"]

    suite = unittest.TestSuite()
    # In case of every keyword - add the corresponding scenario
    if "login" in desired_tests:
        suite = add_login_to_suite(suite)
    if "register" in desired_tests:
        suite = add_registration_to_suite(suite)
    if "flight" in desired_tests:
        suite = add_flight_to_suite(suite)

    # Return the test suite
    return suite
