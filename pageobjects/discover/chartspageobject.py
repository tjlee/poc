from pageobjects import locators
from pageobjects.firefoxConnector import FirefoxConnector
from pageobjects.basepageobject import BasePageObject
from pageobjects.basepageelement import BasePageElement
import urlparse, time


class ChartsPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/profile/charts/"))

        for i in range(60):
            try:
                if self.driver.find_element_by_class_name("charts-list").is_displayed(): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("[error]: .charts-list is not found")

        self.assertEqual("Labbler / Profile / Charts / Archive", self.driver.title)