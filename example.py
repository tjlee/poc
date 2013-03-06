import unittest
from pageobjects.loginpageobject import LoginPageObject
from pageobjects.page.aboutpageobject import AboutPageObject
from pageobjects.page.bookingpageobject import BookingPageObject
from pageobjects.page.calendarpageobject import CalendarPageObject
from pageobjects.page.chartsarchivepageobject import ChartsArchivePageObject
from pageobjects.page.chartsdraftspageobject import ChartsDraftsPageObject
from pageobjects.page.clubspageobject import ClubsPageObject
from pageobjects.page.discographypageobject import DiscographyPageObject
from pageobjects.page.labelspageobject import LabelsPageObject
from pageobjects.page.newsdraftspageobject import NewsDraftsPageObject
from pageobjects.page.pagechartspageobject import PageChartsPageObject
from pageobjects.page.dashboardpageobject import DashboardPageObject
from pageobjects.page.pagemusicuploadpageobject import PageMusicUploadPageObject
from pageobjects.page.pagenewspageobject import PageNewsPageObject
from pageobjects.page.photospageobject import PhotosPageObject
from pageobjects.page.photosuploadpageobject import PhotosUploadPageObject
from pageobjects.page.podcastspageobject import PodcastsPageObject
from pageobjects.page.setspageobject import SetsPageObject
from pageobjects.page.statisticscommentpageobject import StatisticsCommentPageObject
from pageobjects.page.statisticsfollowingpageobject import StatisticsFollowingPageObject
from pageobjects.page.statisticsplaypageobject import StatisticsPlayPageObject
from pageobjects.page.statisticsviewpageobject import StatisticsViewPageObject
from pageobjects.page.videopageobject import VideoPageObject
from pageobjects.page.videouploadpageobject import VideoUploadPageObject
from pageobjects.page.trackspageobject import TracksPageObject

from pageobjects.yourprofile.profile.profiledatapageobject import ProfileDataPageObject
from pageobjects.yourprofile.profile.recentactivitypageobject import RecentActivityPageObject
from pageobjects.yourprofile.profile.eventspageobject import EventsPageObject
from pageobjects.yourprofile.profile.playlistspageobject import PlaylistsPageObject
from pageobjects.yourprofile.profile.profilewallpageobject import ProfileWallPageObject
from pageobjects.yourprofile.profile.socialaccountpageobject import SocialAccountPageObject

from pageobjects.yourprofile.discover.chartspageobject import ChartsPageObject
from pageobjects.yourprofile.discover.musicpageobject import MusicPageObject
from pageobjects.yourprofile.discover.newspageobject import NewsPageObject
from pageobjects.yourprofile.discover.releasespageobject import ReleasesPageObject

from pageobjects.yourprofile.messages.messagespageobject import MessagessPageObject

from pageobjects.firefoxConnector import FirefoxConnector


class PageObjectExample(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.driver = FirefoxConnector.driver
        self.driver.implicitly_wait(30)
        self.base_url = "https://dev.labbler.com/"

    def test_look_extended_statistics(self):
        self.login()

        stat = StatisticsViewPageObject(self.driver, self.base_url)

        stat.view_day_statistic()
        stat.view_week_statistic()
        stat.view_month_statistic()

    def test_navigate_artist_menu(self):

        self.login()

        dpo = DashboardPageObject(self.driver, self.base_url)
        apo = AboutPageObject(self.driver, self.base_url)
        bpo = BookingPageObject(self.driver, self.base_url)
        cpo = CalendarPageObject(self.driver, self.base_url)
        chpo = PageChartsPageObject(self.driver, self.base_url)
        chapo = ChartsArchivePageObject(self.driver, self.base_url)
        chdpo = ChartsDraftsPageObject(self.driver, self.base_url)
        clpo = ClubsPageObject(self.driver, self.base_url)
        dipo = DiscographyPageObject(self.driver, self.base_url)
        lpo = LabelsPageObject(self.driver, self.base_url)
        mpo = PageMusicUploadPageObject(self.driver, self.base_url)
        tpo = TracksPageObject(self.driver, self.base_url)
        ppo = PodcastsPageObject(self.driver, self.base_url)
        spo = SetsPageObject(self.driver, self.base_url)
        npo = PageNewsPageObject(self.driver, self.base_url)
        ndpo = NewsDraftsPageObject(self.driver, self.base_url)
        phpo = PhotosPageObject(self.driver, self.base_url)
        phupo = PhotosUploadPageObject(self.driver, self.base_url)
        svpo = StatisticsViewPageObject(self.driver, self.base_url)
        sppo = StatisticsPlayPageObject(self.driver, self.base_url)
        scpo = StatisticsCommentPageObject(self.driver, self.base_url)
        sfpo = StatisticsFollowingPageObject(self.driver, self.base_url)
        vpo = VideoPageObject(self.driver, self.base_url)
        vupo = VideoUploadPageObject(self.driver, self.base_url)

    def test_navigate_profile_menu(self):
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