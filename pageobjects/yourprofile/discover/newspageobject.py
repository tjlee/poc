import urlparse

from pageobjects.base.basepageobject import BasePageObject
from pageobjects.base.basepageelement import BasePageElement


class NewsPageObject(BasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/profile/news/"))
        self.wait_for_element_displayed_by_class(self.driver, "news-list")
        self.assertEqual("Labbler / Profile / News", self.driver.title)