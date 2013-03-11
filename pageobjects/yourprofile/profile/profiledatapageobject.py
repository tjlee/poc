from pageobjects import locators
from pageobjects.firefoxConnector import FirefoxConnector
from pageobjects.basepageobject import BasePageObject
from pageobjects.basepageelement import BasePageElement
import urlparse, time


class ProfileDataPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/profile/data/"))
        self.wait_for_element_displayed_by_id(self.driver, "id_first_name")
        self.assertEqual("Labbler / Profile / Edit profile", self.driver.title)


