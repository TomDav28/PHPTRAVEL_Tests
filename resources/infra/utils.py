import json

from resources.settings.base_settings import LOGIN_CASES_FILE_PATH, TEST_SETTINGS_FILE_PATH


def get_login_cases():
    with open(LOGIN_CASES_FILE_PATH) as f:
        return json.load(f)

def get_test_suite():
    with open(TEST_SETTINGS_FILE_PATH) as f:
        test_settings = json.load(f)
    