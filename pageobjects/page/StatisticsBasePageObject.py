import time
from pageobjects.basepageobject import BasePageObject
from pageobjects.page import locators


class StatisticsBasePageObject(BasePageObject):
    def view_day_statistic(self):
        self.driver.find_elements_by_css_selector(locators["statistics.day"])[0].click()
        self.wait_for_css_selection_text(self.driver, "span.current-range-title", "Today")

    def view_week_statistic(self):
        self.driver.find_elements_by_css_selector(locators["statistics.day"])[1].click()
        self.wait_for_css_selection_text(self.driver, "span.current-range-title", "This week")

    def view_month_statistic(self):
        self.driver.find_elements_by_css_selector(locators["statistics.day"])[2].click()
        self.wait_for_css_selection_text(self.driver, "span.current-range-title", "This month")

