import urlparse

from pageobjects.page import pages
from pageobjects.page.statisticsbasepageobject import StatisticsBasePageObject

class StatisticsCommentPageObject(StatisticsBasePageObject):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/%s/statistics/comment/" % pages["dirty-south.url"]))
        self.wait_for_element_displayed_by_class(self.driver, "trackset-info")

        #TODO: "Labbler / %s / Statistics"
        self.assertEqual("Labbler / %s" % pages["dirty-south.name"], self.driver.title)