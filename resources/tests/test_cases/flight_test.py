from resources.infra.pages.home_page import HomePage
from resources.infra.pages.search_results_page import SearchResultsPage
from resources.tests.base_tests.base_test import BaseTest, HOMEPAGE_URL


class FlightTests(BaseTest):

    def setUp(self):
        # Go to homepage
        self.browser.go_to_url(HOMEPAGE_URL)
        homepage = HomePage(self.driver)
        self.search_dashboard = homepage.search_dashboard

    def test_nyc_mia_flight(self):
        # Move To Flights tab
        self.search_dashboard.choose_search_flights()

        # Assertions
        self.assertTrue(self.search_dashboard.is_departure_date_picker_displayed())
        self.assertTrue(self.search_dashboard.is_one_way_radio_dispalyed())
        self.assertTrue(self.search_dashboard.is_round_trip_radio_displayed())
        self.assertTrue(self.search_dashboard.is_search_button_displayed())

        # Enter date and move to search results
        self.search_dashboard.set_departure_date(self.param["flight_case"])
        self.search_dashboard.click_search()
        self.browser.wait_for_url_fraction("search")
        self.search_results_page = SearchResultsPage(self.driver)

        # Assertions
        self.assertGreater(self.search_results_page.result_count(), 5)
        self.assertGreater(self.search_results_page.displayed_result_count(), 5)
