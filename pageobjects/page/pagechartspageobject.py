from pageobjects import locators
from pageobjects.page import pages
from pageobjects.firefoxConnector import FirefoxConnector
from pageobjects.basepageobject import BasePageObject
from pageobjects.basepageelement import BasePageElement
import urlparse, time


class PageChartsPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/%s/charts/" % pages["dirty-south.url"]))

        for i in range(60):
            try:
                if self.driver.find_element_by_class_name("charts-list").is_displayed(): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("[error]: .charts-list box is not found")

        #TODO: Change after bug-fix to "Labbler / %s / Charts"
        self.assertEqual("Labbler / %s / Charts / Archive" % pages["dirty-south.name"], self.driver.title)