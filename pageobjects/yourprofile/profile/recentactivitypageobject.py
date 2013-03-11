from pageobjects import locators
from pageobjects.firefoxConnector import FirefoxConnector
from pageobjects.basepageobject import BasePageObject
from pageobjects.basepageelement import BasePageElement
import time, urlparse


class RecentActivityPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/profile/activity/"))
        self.wait_for_element_displayed_by_class(self.driver, "profile-recent-activity")
        self.assertEqual("Labbler / Profile", self.driver.title)