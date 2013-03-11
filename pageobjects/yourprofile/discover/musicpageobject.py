from pageobjects import locators
from pageobjects.firefoxConnector import FirefoxConnector
from pageobjects.basepageobject import BasePageObject
from pageobjects.basepageelement import BasePageElement
import urlparse, time


class MusicPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/profile/audio/"))
        self.wait_for_element_displayed_by_class(self.driver, "song-list")
        self.assertEqual("Labbler / Profile / Music", self.driver.title)