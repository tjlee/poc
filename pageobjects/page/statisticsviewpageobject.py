from pageobjects.page import locators
from pageobjects.page import pages
from pageobjects.firefoxConnector import FirefoxConnector
from pageobjects.basepageobject import BasePageObject
from pageobjects.basepageelement import BasePageElement
import urlparse, time
from pageobjects.page.statisticsbasepageobject import StatisticsBasePageObject


class StatisticsViewPageObject(StatisticsBasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/%s/statistics/view/" % pages["dirty-south.url"]))
        self.wait_for_element_displayed_by_class(self.driver, "trackset-info")

        #TODO: "Labbler / %s / Statistics"
        self.assertEqual("Labbler / %s" % pages["dirty-south.name"], self.driver.title)
