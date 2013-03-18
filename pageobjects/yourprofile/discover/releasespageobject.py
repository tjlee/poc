import urlparse

from pageobjects.base.basepageobject import BasePageObject
from pageobjects.base.basepageelement import BasePageElement


class ReleasesPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/profile/releases/"))
        self.wait_for_element_displayed_by_class(self.driver, "release-list")
        self.assertEqual("Labbler / Profile / Discography", self.driver.title)