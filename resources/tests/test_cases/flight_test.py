from resources.infra.pages.home_page import HomePage
from resources.tests.base_tests.base_test import BaseTest, HOMEPAGE_URL


class FlightTests(BaseTest):

    def setUp(self):
        self.browser.go_to_url(HOMEPAGE_URL)
        homepage = HomePage(self.driver)
        self.search_dashboard = homepage.search_dashboard

    def search_flight(self):
        self.search_dashboard.choose_search_flights()
        # assertions

        self.search_dashboard.fill_fligth_data(self.param["flight_case"])
        self.search_dashboard.click_search()

        pass
