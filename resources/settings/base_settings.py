import os

PROJECT_DIR_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RESOURCES_DIR_PATH = os.path.join(PROJECT_DIR_PATH, "resources")
CHROMEDRIVER_DIR_PATH = os.path.join(RESOURCES_DIR_PATH, "chromedriver")
os.environ["PATH"] += os.pathsep + CHROMEDRIVER_DIR_PATH

TEST_DIR_PATH = os.path.join(RESOURCES_DIR_PATH, "tests")
TEST_DATA_DIR_PATH = os.path.join(TEST_DIR_PATH, "test_data")
LOGIN_CASES_FILE_PATH = os.path.join(TEST_DATA_DIR_PATH, "login_cases.json")



LOGOUT_URL = "https://www.phptravels.net/account/logout/"
LOGIN_URL = "https://www.phptravels.net/login"
HOMEPAGE_URL = "https://www.phptravels.net/"