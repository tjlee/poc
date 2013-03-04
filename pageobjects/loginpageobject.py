from pageobjects import locators
from pageobjects.firefoxConnector import FirefoxConnector
from pageobjects.basepageobject import BasePageObject
from pageobjects.basepageelement import BasePageElement
import time


class SignInElement(BasePageElement):
    def __init__(self):
        self.locator = locators["login.open"]

    def __set__(self, obj, val):
        se = FirefoxConnector.driver
        se.find_element_by_id(self.locator).click()


class UsernameElement(BasePageElement):
    def __init__(self):
        self.locator = locators["login.username"]

    def __set__(self, obj, val):
        se = FirefoxConnector.driver
        se.find_element_by_id(self.locator).send_keys(val)


class PasswordElement(BasePageElement):
    def __init__(self):
        self.locator = locators["login.password"]

    def __set__(self, obj, val):
        se = FirefoxConnector.driver
        se.find_element_by_id(self.locator).send_keys(val)


class LoginPageObject(BasePageObject):
    username = UsernameElement()
    password = PasswordElement()

    def __init__(self, driver, base_url):

        self.driver = driver
        self.driver.get(base_url)

        driver.find_element_by_id(locators["login.open"]).click()

        for i in range(60):
            try:
                if self.driver.find_element_by_id("id_username").is_displayed(): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("[error]: #id_username is not found")

        self.assertEqual("Labbler", self.driver.title)

    def submit(self):
        self.driver.find_element_by_id(locators["login.submit"]).click()

        for i in range(60):
            try:
                if self.driver.title == "Labbler / Profile": break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("[error]: we are not logged in")

        return BasePageObject

