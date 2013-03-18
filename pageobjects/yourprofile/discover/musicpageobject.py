import urlparse

from pageobjects.base.basepageobject import BasePageObject
from pageobjects.base.basepageelement import BasePageElement


class MusicPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/profile/audio/"))
        self.wait_for_element_displayed_by_class(self.driver, "song-list")
        self.assertEqual("Labbler / Profile / Music", self.driver.title)