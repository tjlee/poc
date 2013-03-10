from pageobjects.page import locators
from pageobjects.page import pages
from pageobjects.firefoxConnector import FirefoxConnector
from pageobjects.basepageobject import BasePageObject
from pageobjects.basepageelement import BasePageElement
import urlparse, time


class AboutIframeText(BasePageElement):
    def __init__(self):
        pass

    def __set__(self, instance, value):
        driver = FirefoxConnector.driver
        driver.switch_to_frame(driver.find_elements_by_tag_name('iframe')[0])
        driver.find_elements_by_tag_name('p')[0].send_keys(value)
        driver.switch_to_default_content()


class AboutPageObject(BasePageObject):
    about_iframe_text = AboutIframeText()

    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(urlparse.urljoin(base_url, "/%s/about/" % pages["dirty-south.url"]))

        for i in range(60):
            try:
                if self.driver.find_element_by_class_name("about-page-text").is_displayed(): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("[error]: .about-page-text is not found")

        self.assertEqual("Labbler / %s" % pages["dirty-south.name"], self.driver.title)

    def edit_about_click(self):
        self.driver.find_element_by_css_selector("li.edit a").click()

        for i in range(5):
            try:
                if self.driver.find_element_by_css_selector("div.text_editor").is_displayed(): break
            except:
                pass
            time.sleep(1)

        else:
            self.fail("[error]: can not edit about")

    def submit_click(self):
        self.driver.find_element_by_css_selector(locators["about.submit"]).click()

    def save_click(self):
        self.driver.find_element_by_css_selector(locators["about.save"]).click()
