from pageobjects import locators
from pageobjects.page import pages
from pageobjects.firefoxConnector import FirefoxConnector
from pageobjects.basepageobject import BasePageObject
from pageobjects.basepageelement import BasePageElement
import urlparse, time


class PhotosUploadPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/%s/galleries/create/" % pages["dirty-south.url"]))

        for i in range(60):
            try:
                if self.driver.find_element_by_class_name("photo-upload").is_displayed(): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("[error]: .photo-upload box is not found")

        # TODO: => "Labbler / %s / Photos"
        self.assertEqual("Labbler / %s" % pages["dirty-south.name"], self.driver.title)