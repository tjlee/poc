import urlparse

from pageobjects.page import pages
from pageobjects.base.basepageobject import BasePageObject
from pageobjects.base.basepageelement import BasePageElement


class PodcastsPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/%s/audio/podcasts/" % pages["dirty-south.url"]))
        self.wait_for_element_displayed_by_class(self.driver, "song-list")

        #TODO: => "Labbler / %s / Music / Podcasts"
        self.assertEqual("Labbler / %s / Music" % pages["dirty-south.name"], self.driver.title)