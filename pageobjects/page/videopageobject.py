from pageobjects import locators
from pageobjects.page import pages
from pageobjects.firefoxConnector import FirefoxConnector
from pageobjects.basepageobject import BasePageObject
from pageobjects.basepageelement import BasePageElement
import urlparse, time


class VideoPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/%s/video/" % pages["dirty-south.url"]))

        for i in range(60):
            try:
                if self.driver.find_element_by_class_name("video-thumbnails-list-wrap").is_displayed(): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("[error]: .video-thumbnails-list-wrap box is not found")

        self.assertEqual("Labbler / %s / Video" % pages["dirty-south.name"], self.driver.title)