from pageobjects import locators
from pageobjects.page import pages
from pageobjects.firefoxConnector import FirefoxConnector
from pageobjects.basepageobject import BasePageObject
from pageobjects.basepageelement import BasePageElement
import urlparse, time


class VideoPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/%s/video/" % pages["dirty-south.url"]))
        self.wait_for_element_displayed_by_class(self.driver, "video-thumbnails-list-wrap")
        self.assertEqual("Labbler / %s / Video" % pages["dirty-south.name"], self.driver.title)