from pageobjects import locators
from pageobjects.base import selenium_driver
from pageobjects.base.basepageobject import BasePageObject
from pageobjects.base.basepageelement import BasePageElement


class UsernameElement(BasePageElement):
    def __init__(self):
        self.locator = locators["login.username"]

    def __set__(self, obj, val):
        driver = selenium_driver.driver
        driver.find_element_by_id(self.locator).send_keys(val)


class PasswordElement(BasePageElement):
    def __init__(self):
        self.locator = locators["login.password"]

    def __set__(self, instance, value):
        driver = selenium_driver.driver
        driver.find_element_by_id(self.locator).send_keys(value)


class LoginPageObject(BasePageObject):
    username = UsernameElement()
    password = PasswordElement()

    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(base_url)
        driver.find_element_by_id(locators["login.open"]).click()
        self.wait_for_element_displayed_by_id(self.driver, "id_username")
        self.assertEqual("Labbler", self.driver.title)

    def submit(self):
        self.driver.find_element_by_id(locators["login.submit"]).click()
        self.wait_for_page_title(self.driver, "Labbler / Profile", msg="[error]: we are not logged in")
