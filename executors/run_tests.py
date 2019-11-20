import unittest

from resources.infra.utils import get_test_suite
from HtmlTestRunner import HTMLTestRunner

from resources.settings.base_settings import TEST_REPORT_DESTINATION_FOLDER
from resources.tests.test_cases.login_test import LoginTests


def main():
    suite = get_test_suite()
    runner = HTMLTestRunner(
        output=TEST_REPORT_DESTINATION_FOLDER,
        combine_reports=True,
        report_name="report",
        report_title="{} Test Report"
    )
    runner.run(suite)
