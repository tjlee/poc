import unittest
from pageobjects.loginpageobject import LoginPageObject

from pageobjects.profile.profiledatapageobject import ProfileDataPageObject
from pageobjects.profile.recentactivitypageobject import RecentActivityPageObject
from pageobjects.profile.eventspageobject import EventsPageObject
from pageobjects.profile.playlistspageobject import PlaylistsPageObject
from pageobjects.profile.profilewallpageobject import ProfileWallPageObject
from pageobjects.profile.socialaccountpageobject import SocialAccountPageObject

from pageobjects.discover.chartspageobject import ChartsPageObject
from pageobjects.discover.musicpageobject import MusicPageObject
from pageobjects.discover.newspageobject import NewsPageObject
from pageobjects.discover.releasespageobject import ReleasesPageObject

from pageobjects.messages.messagespageobject import MessagessPageObject

from pageobjects.firefoxConnector import FirefoxConnector


class PageObjectExample(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.driver = FirefoxConnector.driver
        self.driver.implicitly_wait(30)
        self.base_url = "https://dev.labbler.com/"


    def test_navigate_profile_menu(self):
        """
        Discover - Music
        Discover - News
        Discover - Charts
        Discover - Releases

        Profile - Recent activity
        Profile - Profile wall
        Profile - Profile data
        Profile - Social accounts
        Profile - Playlists
        Profile - Events

        Messages
        """

        self.login()

        mpo = MusicPageObject(self.driver, self.base_url)
        npo = NewsPageObject(self.driver, self.base_url)
        cpo = ChartsPageObject(self.driver, self.base_url)
        rpo = ReleasesPageObject(self.driver, self.base_url)

        rapo = RecentActivityPageObject(self.driver, self.base_url)
        pwpo = ProfileWallPageObject(self.driver, self.base_url)
        pdpo = ProfileDataPageObject(self.driver, self.base_url)
        sapo = SocialAccountPageObject(self.driver, self.base_url)
        ppo = PlaylistsPageObject(self.driver, self.base_url)
        epo = EventsPageObject(self.driver, self.base_url)

        msgpo = MessagessPageObject(self.driver, self.base_url)


    def login(self):
        lpo = LoginPageObject(self.driver, self.base_url)

        lpo.username = "tjlee@inbox.ru"
        lpo.password = "Welcome01@"
        lpo.submit()


    def test_login(self):
        self.login()

        pdpo = ProfileDataPageObject(self.driver, self.base_url)
        rapo = RecentActivityPageObject(self.driver, self.base_url)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()