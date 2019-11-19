from selenium.webdriver.common.by import By

from resources.infra.pages.base_page import BasePage
from resources.infra.pages.login_page import LoginPage
from resources.settings.base_settings import LOGIN_URL, REGISTRATION_URL


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.search_dashboard = SearchDashboard(driver)


class SearchDashboard:
    def __init__(self,driver):
        self.driver = driver
        self.flights_tab = (By.CSS_SELECTOR,"a.flights")
        self.one_way_radio = (By.CSS_SELECTOR,"input[type='radio'][value='oneway']")
        self.round_trip_radio = (By.CSS_SELECTOR,"input[type='radio'][value='return']")


    def choose_search_flights(self):
        self.driver.find_element(*self.flights_tab).click()

    def choose_one_way(self):
        self.driver.find_element(*self.one_way_radio).click()

    def choose_round_trip(self):
        self.driver.find_element(*self.round_trip_radio).click()

    def set_flight_origin(self):
        pass

    def set_flight_destination(self):
        pass

    def set_departure_date(self):
        pass

    def set_return_date(self):
        pass

    def click_search(self):
        pass

    def fill_fligth_data(self,flight_data):
        pass