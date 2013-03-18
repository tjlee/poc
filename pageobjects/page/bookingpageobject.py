import urlparse

from pageobjects.page import pages
from pageobjects.base.basepageobject import BasePageObject
from pageobjects.base.basepageelement import BasePageElement


class BookingPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/%s/booking/" % pages["dirty-south.url"]))
        self.wait_for_element_displayed_by_multiple_classes(self.driver, "booking", "empty-noises-big")
        self.assertEqual("Labbler / %s" % pages["dirty-south.name"], self.driver.title)