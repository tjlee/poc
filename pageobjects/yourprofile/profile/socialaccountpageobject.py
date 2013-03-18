import urlparse

from pageobjects.base.basepageobject import BasePageObject
from pageobjects.base.basepageelement import BasePageElement


class SocialAccountPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/profile/social/"))
        self.wait_for_element_displayed_by_class(self.driver, "assign_new_social")
        self.assertEqual("Labbler / Profile / Social accounts", self.driver.title)