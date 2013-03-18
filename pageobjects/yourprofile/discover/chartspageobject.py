import urlparse

from pageobjects.base.basepageobject import BasePageObject
from pageobjects.base.basepageelement import BasePageElement


class ChartsPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/profile/charts/"))
        self.wait_for_element_displayed_by_class(self.driver, "charts-list")
        self.assertEqual("Labbler / Profile / Charts / Archive", self.driver.title)