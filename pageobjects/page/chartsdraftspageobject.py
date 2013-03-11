from pageobjects import locators
from pageobjects.page import pages
from pageobjects.firefoxConnector import FirefoxConnector
from pageobjects.basepageobject import BasePageObject
from pageobjects.basepageelement import BasePageElement
import urlparse, time


class ChartsDraftsPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/%s/charts/drafts/" % pages["dirty-south.url"]))
        self.wait_for_element_displayed_by_class(self.driver, "charts-list")

        #TODO: change after bug fixed "Labbler / %s / Charts / Drafts"
        self.assertEqual("Labbler / %s / Charts / Archive" % pages["dirty-south.name"], self.driver.title)