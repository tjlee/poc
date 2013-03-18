import urlparse

from selenium.webdriver.common.keys import Keys

from pageobjects.page import locators
from pageobjects.page import pages
from pageobjects.base.firefoxConnector import FirefoxConnector
from pageobjects.base.basepageobject import BasePageObject
from pageobjects.base.basepageelement import BasePageElement


class NewsEntryTitleElement(BasePageElement):
    def __init__(self):
        self.locator = locators["news.title"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_id(self.locator).clear()
        driver.find_element_by_id(self.locator).send_keys(value)


class NewsEntryTextElement(BasePageElement):
    def __init__(self):
        pass

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.switch_to_frame(driver.find_elements_by_tag_name('iframe')[0])
        driver.find_element_by_tag_name('body').send_keys(value)
        driver.switch_to_default_content()


class PageNewsPageObject(BasePageObject):
    news_entry_title_element = NewsEntryTitleElement()
    news_entry_text_element = NewsEntryTextElement()

    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/%s/news/" % pages["dirty-south.url"]))
        self.wait_for_element_displayed_by_class(self.driver, "news-list")
        self.assertEqual("Labbler / %s / News" % pages["dirty-south.name"], self.driver.title)

    def add_news_btn_click(self):
        self.driver.find_element_by_css_selector(locators["news.add"]).click()
        self.wait_for_element_displayed_by_id(self.driver, "id_title")
        self.assertEqual("Labbler / %s / Create newsentry" % pages["dirty-south.name"], self.driver.title)

    def submit_news_entry(self, news_title="test title"):
        self.driver.find_element_by_css_selector(locators["release.publish"]).click()
        self.wait_for_element_displayed_by_css(self.driver, "li.news-list-item")
        self.assertEqual("Labbler / %s / %s" % (pages["dirty-south.name"], news_title), self.driver.title)

    def comment_news_by_title(self, comment="lololo3", news_title="test"):
        self.driver.find_element_by_link_text(news_title).click()
        self.wait_for_element_displayed_by_css(self.driver, "li.news-list-item")

        self.driver.find_element_by_id("id_comment").send_keys(comment)
        self.driver.find_element_by_id("id_comment").send_keys(Keys.RETURN)
        self.wait_for_element_displayed_by_css(self.driver, "span.js-remove-comment", timeout=5)

    def edit_news_ty_title(self, news_title="test"):
        self.driver.find_element_by_link_text(news_title).click()
        self.wait_for_element_displayed_by_css(self.driver, "li.news-list-item")
        self.driver.find_element_by_css_selector(locators["news.edit"]).click()
        self.wait_for_element_displayed_by_id(self.driver, locators["news.title"])
        self.assertEqual('Labbler / %s / Edit "%s"' % (pages["dirty-south.name"], news_title), self.driver.title)

    def delete_news_by_title(self, news_title="test"):
        self.edit_news_ty_title(news_title)
        self.driver.find_element_by_css_selector(locators["chart.delete"]).click()
        self.wait_for_element_displayed_by_css(self.driver, "input.entry-delete-button", timeout=5)
        self.driver.find_element_by_css_selector(locators["news.delete_popup"]).click()
        self.wait_for_element_displayed_by_css(self.driver, "li.news-list-item")


