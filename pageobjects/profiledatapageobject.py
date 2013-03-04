from pageobjects import locators
from pageobjects.firefoxConnector import FirefoxConnector
from pageobjects.basepageobject import BasePageObject
from pageobjects.basepageelement import BasePageElement
import urlparse, time

#https://dev.labbler.com/profile/data/
class ProfileDataPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/profile/data/"))

        for i in range(60):
            try:
                if self.driver.find_element_by_id("id_first_name").is_displayed(): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("[error]: #id_first_name is not found")

        self.assertEqual("Labbler / Profile / Edit profile", self.driver.title)


