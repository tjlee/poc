from pageobjects import locators
from pageobjects.page import pages
from pageobjects.firefoxConnector import FirefoxConnector
from pageobjects.basepageobject import BasePageObject
from pageobjects.basepageelement import BasePageElement
import urlparse, time


class LabelsPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/%s/labels/" % pages["dirty-south.url"]))

        for i in range(60):
            try:
                if self.driver.find_element_by_class_name("label").is_displayed() or\
                    self.driver.find_element_by_class_name("empty-noises-big").is_displayed() : break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("[error]: .label or empty-noises-big is not found")

        #TODO: => "Labbler / %s / Labels
        self.assertEqual("Labbler / %s" % pages["dirty-south.name"], self.driver.title)