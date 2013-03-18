import urlparse

from selenium.webdriver.common.keys import Keys

from pageobjects.page import locators
from pageobjects.page import pages
from pageobjects.base.firefoxConnector import FirefoxConnector
from pageobjects.base.basepageobject import BasePageObject
from pageobjects.base.basepageelement import BasePageElement


class ReleaseTitleElement(BasePageElement):
    def __init__(self):
        self.locator = locators["release.title"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_id(self.locator).clear()
        driver.find_element_by_id(self.locator).send_keys(value)


class ReleaseArtistElement(BasePageElement):
    def __init__(self):
        self.locator = locators["release.artist"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)


class ReleaseLabelElement(BasePageElement):
    def __init__(self):
        self.locator = locators["release.label"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)


class ReleaseDateElement(BasePageElement):
    def __init__(self):
        self.locator = locators["release.date"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.execute_script("$('#id_release_date').attr('readonly',false)")
        driver.find_element_by_id(self.locator).send_keys(value)

#
# class ReleaseGenreElement(BasePageElement):
#     def __init__(self):
#         self.locator = locators["release.genre"]
#
#     def __set__(self, instance, value):
#         driver = FirefoxConnector.driver
#         # TODO: due to cusel can be problems
#         driver.find_element_by_css_selector(self.locator).send_keys(value)


class ReleaseFirstTrackElement(BasePageElement):
    def __init__(self):
        self.locator = locators["release.first_track"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)


class ReleaseFirstArtistElement(BasePageElement):
    def __init__(self):
        self.locator = locators["release.first_artist"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)


class ReleaseFirstMixElement(BasePageElement):
    def __init__(self):
        self.locator = locators["release.first_mix"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)


class ReleaseFirstTrackHoursElement(BasePageElement):
    def __init__(self):
        self.locator = locators["release.first_hours"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_id(self.locator).clear()
        driver.find_element_by_id(self.locator).send_keys(value)


class ReleaseFirstTrackMinutesElement(BasePageElement):
    def __init__(self):
        self.locator = locators["release.first_minutes"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_id(self.locator).clear()
        driver.find_element_by_id(self.locator).send_keys(value)


class ReleaseFirstTrackSecondsElement(BasePageElement):
    def __init__(self):
        self.locator = locators["release.first_seconds"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_id(self.locator).clear()
        driver.find_element_by_id(self.locator).send_keys(value)


#-- 2

class ReleaseSecondTrackElement(BasePageElement):
    def __init__(self):
        self.locator = locators["release.second_track"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)


class ReleaseSecondArtistElement(BasePageElement):
    def __init__(self):
        self.locator = locators["release.second_artist"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)


class ReleaseSecondMixElement(BasePageElement):
    def __init__(self):
        self.locator = locators["release.second_mix"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)


class ReleaseSecondTrackHoursElement(BasePageElement):
    def __init__(self):
        self.locator = locators["release.second_hours"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_id(self.locator).clear()
        driver.find_element_by_id(self.locator).send_keys(value)


class ReleaseSecondTrackMinutesElement(BasePageElement):
    def __init__(self):
        self.locator = locators["release.second_minutes"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_id(self.locator).clear()
        driver.find_element_by_id(self.locator).send_keys(value)


class ReleaseSecondTrackSecondsElement(BasePageElement):
    def __init__(self):
        self.locator = locators["release.second_seconds"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_id(self.locator).clear()
        driver.find_element_by_id(self.locator).send_keys(value)


#-- 3

class ReleaseThirdTrackElement(BasePageElement):
    def __init__(self):
        self.locator = locators["release.third_track"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)


class ReleaseThirdArtistElement(BasePageElement):
    def __init__(self):
        self.locator = locators["release.third_artist"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)


class ReleaseThirdMixElement(BasePageElement):
    def __init__(self):
        self.locator = locators["release.third_mix"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)


class ReleaseThirdTrackHoursElement(BasePageElement):
    def __init__(self):
        self.locator = locators["release.third_hours"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_id(self.locator).clear()
        driver.find_element_by_id(self.locator).send_keys(value)


class ReleaseThirdTrackMinutesElement(BasePageElement):
    def __init__(self):
        self.locator = locators["release.third_minutes"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_id(self.locator).clear()
        driver.find_element_by_id(self.locator).send_keys(value)


class ReleaseThirdTrackSecondsElement(BasePageElement):
    def __init__(self):
        self.locator = locators["release.third_seconds"]

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.find_element_by_id(self.locator).clear()
        driver.find_element_by_id(self.locator).send_keys(value)


class DiscographyPageObject(BasePageObject):
    release_title = ReleaseTitleElement()
    release_artist = ReleaseArtistElement()
    release_label = ReleaseLabelElement()
    release_date = ReleaseDateElement()
    # release_genre = ReleaseGenreElement()

    release_first_track = ReleaseFirstTrackElement()
    release_first_artist = ReleaseFirstArtistElement()
    release_first_mix = ReleaseFirstMixElement()
    release_first_hours = ReleaseFirstTrackHoursElement()
    release_first_minutes = ReleaseFirstTrackMinutesElement()
    release_first_seconds = ReleaseFirstTrackSecondsElement()

    release_second_track = ReleaseSecondTrackElement()
    release_second_artist = ReleaseSecondArtistElement()
    release_second_mix = ReleaseSecondMixElement()
    release_second_hours = ReleaseSecondTrackHoursElement()
    release_second_minutes = ReleaseSecondTrackMinutesElement()
    release_second_seconds = ReleaseSecondTrackSecondsElement()

    release_third_track = ReleaseThirdTrackElement()
    release_third_artist = ReleaseThirdArtistElement()
    release_third_mix = ReleaseThirdMixElement()
    release_third_hours = ReleaseThirdTrackHoursElement()
    release_third_minutes = ReleaseThirdTrackMinutesElement()
    release_third_seconds = ReleaseThirdTrackSecondsElement()

    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/%s/discography/" % pages["dirty-south.url"]))
        self.wait_for_element_displayed_by_class(self.driver, "release-list")
        self.assertEqual("Labbler / %s / Discography" % pages["dirty-south.name"], self.driver.title)

    def add_release_btn_click(self):
        self.driver.find_element_by_css_selector(locators["release.add"]).click()
        self.wait_for_element_displayed_by_id(self.driver, "id_title")
        self.assertEqual("Labbler / %s / Create release" % pages["dirty-south.name"], self.driver.title)

    def select_genre(self):
        """
        Hardcoded to "Chill out"
        """
        self.driver.find_element_by_id("cuselFrame-id_genre").click()
        self.driver.find_element_by_css_selector('#cusel-scroll-id_genre span[val="2"]').click()

    def publish_release(self, release_name="test_release"):
        self.driver.find_element_by_css_selector(locators["release.publish"]).click()
        self.wait_for_element_displayed_by_css(self.driver, "div.release-entry")
        self.assertEqual("Labbler / %s / %s" % (pages["dirty-south.name"], release_name), self.driver.title)

    def edit_release_by_name(self, release_name):
        self.driver.find_element_by_link_text(release_name).click() # selecting first one
        self.wait_for_element_displayed_by_css(self.driver, "div.release-track-list")
        self.driver.find_element_by_css_selector(locators["release.edit"]).click()
        self.wait_for_element_displayed_by_id(self.driver, locators["release.title"])
        self.assertEqual('Labbler / %s / Edit "%s"' % (pages["dirty-south.name"], release_name), self.driver.title)

    def comment_release_by_name(self, comment="lololo3", release_name="test"):
        self.driver.find_element_by_link_text(release_name).click()
        self.wait_for_element_displayed_by_css(self.driver, "div.release-track-list")

        self.driver.find_element_by_id("id_comment").send_keys(comment)
        self.driver.find_element_by_id("id_comment").send_keys(Keys.RETURN)
        self.wait_for_element_displayed_by_css(self.driver, "span.js-remove-comment", timeout=5)

    def delete_release_by_name(self, release_name="release title"):
        self.edit_release_by_name(release_name)
        self.driver.find_element_by_id(locators["release.delete"]).click()
        self.wait_for_element_displayed_by_css(self.driver, "input.entry-delete-button", timeout=5)
        self.driver.find_element_by_css_selector(locators["release.delete_popup"]).click()
        self.wait_for_element_displayed_by_css(self.driver, "ul.release-list")
