from pageobjects import locators
from pageobjects.firefoxConnector import FirefoxConnector
from pageobjects.basepageobject import BasePageObject
from pageobjects.basepageelement import BasePageElement
import time, urlparse


class PlaylistsPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/profile/playlists/"))
        self.wait_for_element_displayed_by_class(self.driver, "own_playlists")
        self.assertEqual("Labbler / Profile / Playlists", self.driver.title)