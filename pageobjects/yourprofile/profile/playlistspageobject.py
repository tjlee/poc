import urlparse

from pageobjects.base.basepageobject import BasePageObject
from pageobjects.base.basepageelement import BasePageElement


class PlaylistsPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/profile/playlists/"))
        self.wait_for_element_displayed_by_class(self.driver, "own_playlists")
        self.assertEqual("Labbler / Profile / Playlists", self.driver.title)