import unittest

from resources.infra.utils import get_login_cases
from resources.tests.base_tests.param_base_test import ParametrizedTestCase
from resources.tests.test_cases.login_test import LoginTests

if __name__ == "__main__":
    suite = unittest.TestSuite()
    login_cases = get_login_cases()
    for login_case in login_cases["successful"]:
        suite.addTest(ParametrizedTestCase.parametrize(
            LoginTests,
            param={
                "should-pass": True,
                "login_case": login_case
            }
        ))
    unittest.TextTestRunner(verbosity=2).run(suite)
