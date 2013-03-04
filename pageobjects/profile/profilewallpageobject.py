from pageobjects import locators
from pageobjects.firefoxConnector import FirefoxConnector
from pageobjects.basepageobject import BasePageObject
from pageobjects.basepageelement import BasePageElement
import time, urlparse


class ProfileWallPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/profile/wall/"))

        for i in range(60):
            try:
                if self.driver.find_element_by_class_name("profile-recent-activity-header").is_displayed(): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("[error]: .profile-recent-activity-header is not found")

        self.assertEqual("Labbler / Profile", self.driver.title)