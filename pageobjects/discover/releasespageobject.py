from pageobjects import locators
from pageobjects.firefoxConnector import FirefoxConnector
from pageobjects.basepageobject import BasePageObject
from pageobjects.basepageelement import BasePageElement
import urlparse, time


class ReleasesPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/profile/releases/"))

        for i in range(60):
            try:
                if self.driver.find_element_by_class_name("release-list").is_displayed(): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("[error]: .release-list is not found")

        self.assertEqual("Labbler / Profile / Discography", self.driver.title)