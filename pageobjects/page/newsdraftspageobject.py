import urlparse

from pageobjects.page import pages
from pageobjects.base.basepageobject import BasePageObject
from pageobjects.base.basepageelement import BasePageElement


class NewsDraftsPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/%s/news/drafts/" % pages["dirty-south.url"]))
        self.wait_for_element_displayed_by_class(self.driver, "news-list")

        # TODO: => "Labbler / %s / News / Drafts"
        self.assertEqual("Labbler / %s / News" % pages["dirty-south.name"], self.driver.title)