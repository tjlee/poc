import urlparse

from pageobjects.page import pages
from pageobjects.base.basepageobject import BasePageObject
from pageobjects.base.basepageelement import BasePageElement


class ClubsPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/%s/clubs/" % pages["dirty-south.url"]))
        self.wait_for_element_displayed_by_multiple_classes(self.driver, "club", "empty-noises-big")

        #TODO: => "Labbler / %s / Clubs
        self.assertEqual("Labbler / %s" % pages["dirty-south.name"], self.driver.title)