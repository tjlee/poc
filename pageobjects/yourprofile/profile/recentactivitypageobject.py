import urlparse

from pageobjects.base.basepageobject import BasePageObject
from pageobjects.base.basepageelement import BasePageElement


class RecentActivityPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/profile/activity/"))
        self.wait_for_element_displayed_by_class(self.driver, "profile-recent-activity")
        self.assertEqual("Labbler / Profile", self.driver.title)