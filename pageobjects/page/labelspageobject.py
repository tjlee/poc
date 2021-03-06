import urlparse

from pageobjects.page import pages
from pageobjects.base.basepageobject import BasePageObject
from pageobjects.base.basepageelement import BasePageElement


class LabelsPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/%s/labels/" % pages["dirty-south.url"]))
        self.wait_for_element_displayed_by_multiple_classes(self.driver, "label", "empty-noises-big")

        #TODO: => "Labbler / %s / Labels
        self.assertEqual("Labbler / %s" % pages["dirty-south.name"], self.driver.title)