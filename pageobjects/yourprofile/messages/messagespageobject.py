import urlparse

from pageobjects.base.basepageobject import BasePageObject
from pageobjects.base.basepageelement import BasePageElement


class MessagessPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/profile/messages/"))
        self.wait_for_element_displayed_by_class(self.driver, "messaging-page")
        self.assertEqual("Labbler / Messages", self.driver.title)