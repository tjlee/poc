import time
from pageobjects.basepageobject import BasePageObject
from pageobjects.page import locators


class StatisticsBasePageObject(BasePageObject):
    def view_day_statistic(self):
        self.driver.find_elements_by_css_selector(locators["statistics.day"])[0].click()

        for i in range(5):
            try:
                if self.driver.find_element_by_css_selector("span.current-range-title").text == "Today": break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("[error]: statistic is not shown")


    def view_week_statistic(self):
        self.driver.find_elements_by_css_selector(locators["statistics.day"])[1].click()

        for i in range(5):
            try:
                if self.driver.find_element_by_css_selector("span.current-range-title").text == "This week": break
            except:
                pass
            time.sleep(1)

        else:
            self.fail("[error]: statistic is not shown")


    def view_month_statistic(self):
        self.driver.find_elements_by_css_selector(locators["statistics.day"])[2].click()

        for i in range(5):
            try:
                if self.driver.find_element_by_css_selector("span.current-range-title").text == "This month": break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("[error]: statistic is not shown")


