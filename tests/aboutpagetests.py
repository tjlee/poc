import unittest
from pageobjects.base import selenium_driver
from pageobjects.login.loginpageobject import LoginPageObject
from pageobjects.page.aboutpageobject import AboutPageObject


class AboutPageTests(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.driver = selenium_driver.connect()
        self.driver.implicitly_wait(10)
        self.base_url = selenium_driver.base_url

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_edit_page_about(self):
        self.login()

        apo = AboutPageObject(self.driver, self.base_url)
        apo.edit_about_click()
        apo.about_iframe_text = "additional text"
        apo.submit_click()

    def login(self):
        lpo = LoginPageObject(self.driver, self.base_url)

        lpo.username = "tjlee@inbox.ru"
        lpo.password = "Welcome01@"
        lpo.submit()


if __name__ == "__main__":
    unittest.main()