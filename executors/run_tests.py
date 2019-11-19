import unittest

from resources.infra.utils import get_test_suite
from resources.tests.base_tests.param_base_test import ParametrizedTestCase
from resources.tests.test_cases.login_test import LoginTests

if __name__ == "__main__":
    suite = get_test_suite()
    unittest.TextTestRunner(verbosity=2).run(suite)
