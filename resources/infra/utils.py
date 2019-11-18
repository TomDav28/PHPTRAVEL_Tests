import json

from resources.settings.base_settings import LOGIN_CASES_FILE_PATH


def get_login_cases():
    with open(LOGIN_CASES_FILE_PATH) as f:
        return json.load(f)