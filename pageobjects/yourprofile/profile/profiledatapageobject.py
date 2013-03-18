import urlparse

from pageobjects.base.basepageobject import BasePageObject
from pageobjects.base.basepageelement import BasePageElement


class ProfileDataPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/profile/data/"))
        self.wait_for_element_displayed_by_id(self.driver, "id_first_name")
        self.assertEqual("Labbler / Profile / Edit profile", self.driver.title)


