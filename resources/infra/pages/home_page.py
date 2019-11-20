from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from resources.infra.pages.base_page import BasePage
from resources.infra.pages.login_page import LoginPage
from resources.settings.base_settings import LOGIN_URL, REGISTRATION_URL
import datetime


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.search_dashboard = SearchDashboard(driver)


class SearchDashboard:
    def __init__(self, driver):
        self.driver = driver
        self.flights_tab = (By.CSS_SELECTOR, "a.flights")
        self.one_way_radio = (By.CSS_SELECTOR, ".custom-radio:nth-of-type(1)")
        self.round_trip_radio = (By.CSS_SELECTOR, ".custom-radio:nth-of-type(2)")
        self.flight_departure_date_picker = (By.CSS_SELECTOR, "#FlightsDateStart")
        self.search_button = (By.CSS_SELECTOR, "div.col-md-1 button")

    def choose_search_flights(self):
        self.driver.find_element(*self.flights_tab).click()

    def set_departure_date(self, flight_case):
        str_date = self.get_date_from_case(flight_case)
        self.driver.execute_script("arguments[0].value = arguments[1]",
                                   self.driver.find_element(*self.flight_departure_date_picker),
                                   str_date)

    def get_date_from_case(self, flight_case):
        year = datetime.date.today().year
        month = flight_case["month"]
        day = flight_case["day"]
        if datetime.date.today() > datetime.date(year, month, day): year += 1
        return "{year}-{month}-{day}".format(
            year=year,
            month=month,
            day=day)

    def click_search(self):
        self.driver.find_element(*self.search_button).click()

    def is_one_way_radio_dispalyed(self):
        try:
            return self.driver.find_element(*self.one_way_radio).is_displayed()
        except NoSuchElementException:
            return False

    def is_round_trip_radio_displayed(self):
        try:
            return self.driver.find_element(*self.round_trip_radio).is_displayed()
        except NoSuchElementException:
            return False

    def is_departure_date_picker_displayed(self):
        try:
            return self.driver.find_element(*self.flight_departure_date_picker).is_displayed()
        except NoSuchElementException:
            return False

    def is_search_button_displayed(self):
        try:
            return self.driver.find_element(*self.search_button).is_displayed()
        except NoSuchElementException:
            return False
