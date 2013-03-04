from pageobjects.loginpageobject import LoginPageObject
from pageobjects.profiledatapageobject import ProfileDataPageObject
from pageobjects.recentactivitypageobject import RecentActivityPageObject
from pageobjects.firefoxConnector import FirefoxConnector

import sys, unittest, re, time, os.path, logging

class PageObjectExample(unittest.TestCase):

    def setUp(self):
        self.verificationErrors = []
        self.selenium = FirefoxConnector.driver
        self.selenium.implicitly_wait(30)
        self.base_url = "https://dev.labbler.com/"

    def test_login(self):


        lpo = LoginPageObject(self.selenium, self.base_url)

        lpo.username = "tjlee@inbox.ru"
        lpo.password = "Welcome01@"
        lpo.submit()


        pdpo = ProfileDataPageObject(self.selenium, self.base_url)
        rapo = RecentActivityPageObject(self.selenium, self.base_url)

    def tearDown(self):
        self.selenium.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()