import urlparse

from pageobjects.page import pages
from pageobjects.base.basepageobject import BasePageObject
from pageobjects.base.basepageelement import BasePageElement


class SetsPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/%s/audio/sets/" % pages["dirty-south.url"]))
        self.wait_for_element_displayed_by_class(self.driver, "set-list")
        self.assertEqual("Labbler / %s / Sets" % pages["dirty-south.name"], self.driver.title)