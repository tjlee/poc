from selenium.webdriver.common.keys import Keys
from pageobjects.page import locators
from pageobjects.page import pages
from pageobjects.firefoxConnector import FirefoxConnector
from pageobjects.basepageobject import BasePageObject
from pageobjects.basepageelement import BasePageElement
import urlparse, time


class ChartTitleElement(BasePageElement):
    def __init__(self):
        self.locator = locators["chart.title"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_id(self.locator).clear()
        driver.find_element_by_id(self.locator).send_keys(value)


class ChartDescriptionElement(BasePageElement):
    def __init__(self):
        self.locator = locators["chart.description"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_id(self.locator).send_keys(value)


class ChartBuyLinkElement(BasePageElement):
    def __int__(self):
        self.locator = locators["chart.buy_link"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_id(self.locator).send_keys(value)


class ChartFirstLineNameElement(BasePageElement):
    def __init__(self):
        self.locator = locators["chart.first_name"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_name(self.locator).send_keys(value)


class ChartFirstLineArtistElement(BasePageElement):
    def __init__(self):
        self.locator = locators["chart.first_artist"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_name(self.locator).send_keys(value)


class ChartFirstLineLabelElement(BasePageElement):
    def __init__(self):
        self.locator = locators["chart.first_label"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_name(self.locator).send_keys(value)


class ChartSecondLineNameElement(BasePageElement):
    def __init__(self):
        self.locator = locators["chart.second_name"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_name(self.locator).send_keys(value)


class ChartSecondLineArtistElement(BasePageElement):
    def __init__(self):
        self.locator = locators["chart.second_artist"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_name(self.locator).send_keys(value)


class ChartSecondLineLabelElement(BasePageElement):
    def __init__(self):
        self.locator = locators["chart.second_label"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_name(self.locator).send_keys(value)


class ChartThirdLineNameElement(BasePageElement):
    def __init__(self):
        self.locator = locators["chart.third_name"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_name(self.locator).send_keys(value)


class ChartThirdLineArtistElement(BasePageElement):
    def __init__(self):
        self.locator = locators["chart.third_artist"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_name(self.locator).send_keys(value)


class ChartThirdLineLabelElement(BasePageElement):
    def __init__(self):
        self.locator = locators["chart.third_label"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_name(self.locator).send_keys(value)


class PageChartsPageObject(BasePageObject):
    chart_title = ChartTitleElement()
    chart_description = ChartDescriptionElement()
    chart_buy_link = ChartBuyLinkElement()

    chart_first_name = ChartFirstLineNameElement()
    chart_first_artist = ChartFirstLineArtistElement()
    chart_first_label = ChartFirstLineLabelElement()

    chart_second_name = ChartSecondLineNameElement()
    chart_second_artist = ChartSecondLineArtistElement()
    chart_second_label = ChartSecondLineLabelElement()

    chart_third_name = ChartThirdLineNameElement()
    chart_third_artist = ChartThirdLineArtistElement()
    chart_third_label = ChartThirdLineLabelElement()

    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/%s/charts/" % pages["dirty-south.url"]))
        self.wait_for_element_displayed_by_css(self.driver, "ul.charts-list")
        #TODO: Change after bug-fix to "Labbler / %s / Charts"
        self.assertEqual("Labbler / %s / Charts / Archive" % pages["dirty-south.name"], self.driver.title)

    def add_chart(self):
        self.driver.find_element_by_css_selector(locators["chart.add"]).click()
        self.wait_for_element_displayed_by_id(self.driver, "id_title")
        self.assertEqual("Labbler / %s / Create chart" % pages["dirty-south.name"], self.driver.title)

    def publish_chart(self, chart_name="test"):
        self.driver.find_element_by_css_selector(locators["chart.publish"]).click()
        self.wait_for_element_displayed_by_css(self.driver, "ul.charts-list")
        #TODO: Change after bug-fix to "Labbler / %s / Charts"
        self.assertEqual("Labbler / %s / %s" % (pages["dirty-south.name"], chart_name), self.driver.title)

    def edit_chart_by_name(self, chart_name="test"):
        self.driver.find_element_by_link_text(chart_name).click() # selecting first one
        self.wait_for_element_displayed_by_css(self.driver, "ul.charts-list")
        self.driver.find_element_by_css_selector(locators["chart.edit"]).click()
        self.wait_for_element_displayed_by_id(self.driver, locators["chart.title"])
        self.assertEqual("Labbler / %s / Edit chart" % pages["dirty-south.name"], self.driver.title)

    def delete_chart_by_name(self, chart_name="test"):
        self.edit_chart_by_name(chart_name)
        self.driver.find_element_by_css_selector(locators["chart.delete"]).click()
        self.wait_for_element_displayed_by_css(self.driver, "input.entry-delete-button", timeout=5)
        self.driver.find_element_by_css_selector(locators["chart.delete_popup"]).click()
        self.wait_for_element_displayed_by_css(self.driver, "ul.charts-list")

    def comment_chart_by_name(self, comment="lololo3", chart_name="test"):
        self.driver.find_element_by_link_text(chart_name).click()
        self.wait_for_element_displayed_by_css(self.driver, "ul.charts-list")

        self.driver.find_element_by_id("id_comment").send_keys(comment)
        self.driver.find_element_by_id("id_comment").send_keys(Keys.RETURN)
        self.wait_for_element_displayed_by_css(self.driver, "span.js-remove-comment", timeout=5)



