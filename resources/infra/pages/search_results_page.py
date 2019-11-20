from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from resources.infra.pages.base_page import BasePage


class SearchResultsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.search_results_list = (By.CSS_SELECTOR, "ul#LIST > li")
        self.search_result_format = (By.CSS_SELECTOR, "ul#LIST > li:nth-of-type({n}) .theme-search-results-item-preview")

    def result_count(self):
        return len(self.driver.find_elements(*self.search_results_list))

    def displayed_result_count(self):
        flag_list = []
        for i in range(self.result_count()):
            search_result = (By.CSS_SELECTOR, self.search_result_format[1].format(n = i + 1))
            if not self.is_search_result_displayed(search_result): return i
        return self.result_count()

    def is_search_result_displayed(self, search_result):
        try:
            return self.driver.find_element(*search_result).is_displayed()
        except NoSuchElementException:
            return False
