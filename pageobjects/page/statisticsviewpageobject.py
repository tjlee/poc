from pageobjects.page import locators
from pageobjects.page import pages
from pageobjects.firefoxConnector import FirefoxConnector
from pageobjects.basepageobject import BasePageObject
from pageobjects.basepageelement import BasePageElement
import urlparse, time

class StatisticsViewPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/%s/statistics/view/" % pages["dirty-south.url"]))

        for i in range(60):
            try:
                if self.driver.find_element_by_class_name("trackset-info").is_displayed(): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("[error]: .trackset-info box is not found")

        #TODO: "Labbler / %s / Statistics"
        self.assertEqual("Labbler / %s" % pages["dirty-south.name"], self.driver.title)

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

