import urlparse

from pageobjects.page import pages
from pageobjects.base.basepageobject import BasePageObject
from pageobjects.base.basepageelement import BasePageElement


class PhotosUploadPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/%s/galleries/create/" % pages["dirty-south.url"]))
        self.wait_for_element_displayed_by_class(self.driver, "photo-upload")

        # TODO: => "Labbler / %s / Photos"
        self.assertEqual("Labbler / %s" % pages["dirty-south.name"], self.driver.title)