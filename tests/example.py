import unittest
from pageobjects.login.loginpageobject import LoginPageObject
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
from pageobjects.page.statisticssharingpageobject import StatisticsSharingPageObject
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

from pageobjects.base.firefoxConnector import FirefoxConnector


class PageObjectExample(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.driver = FirefoxConnector.driver
        self.driver.implicitly_wait(30)
        self.base_url = FirefoxConnector.base_url

    def test_look_extended_statistics(self):
        self.login()

        stat = StatisticsViewPageObject(self.driver, self.base_url)
        stat.view_day_statistic()
        stat.view_week_statistic()
        stat.view_month_statistic()

        stat2 = StatisticsPlayPageObject(self.driver, self.base_url)
        stat2.view_day_statistic()
        stat2.view_week_statistic()
        stat2.view_month_statistic()

        stat3 = StatisticsCommentPageObject(self.driver, self.base_url)
        stat3.view_day_statistic()
        stat3.view_week_statistic()
        stat3.view_month_statistic()

        stat4 = StatisticsFollowingPageObject(self.driver, self.base_url)
        stat4.view_day_statistic()
        stat4.view_week_statistic()
        stat4.view_month_statistic()

        stat5 = StatisticsSharingPageObject(self.driver, self.base_url)
        stat5.view_day_statistic()
        stat5.view_week_statistic()
        stat5.view_month_statistic()

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
        sspo = StatisticsSharingPageObject(self.driver, self.base_url)
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

    def test_edit_page_about(self):
        self.login()

        apo = AboutPageObject(self.driver, self.base_url)
        apo.edit_about_click()
        apo.about_iframe_text = "additional text"
        apo.submit_click()

    def test_add_chart(self):
        self.login()
        self.add_chart("test")

    def test_edit_chart(self):
        self.login()

        chart_name = "t2est2"
        new_chart_name = "t3est3"

        self.add_chart(chart_name)
        cpo = PageChartsPageObject(self.driver, self.base_url)

        cpo.edit_chart_by_name(chart_name)
        cpo.chart_title = new_chart_name
        cpo.publish_chart(new_chart_name)

        cpo.__init__(self.driver, self.base_url)
        cpo.delete_chart_by_name(new_chart_name)

    def test_comment_chart_by_name(self):
        self.login()
        cpo = PageChartsPageObject(self.driver, self.base_url)
        chart_name = "t3est3"
        cpo.comment_chart_by_name(comment="now way", chart_name=chart_name)

    def test_comment_release_by_name(self):
        self.login()
        dpo = DiscographyPageObject(self.driver, self.base_url)
        release_name = "new title forever"
        dpo.comment_release_by_name(comment="to to ro bo", release_name=release_name)

    def add_chart(self, chart_title="test"):
        cpo = PageChartsPageObject(self.driver, self.base_url)
        cpo.add_chart_btn_click()

        cpo.chart_title = chart_title
        cpo.chart_description = "test description"

        cpo.chart_first_artist = "lalala"
        cpo.chart_first_label = "lalala"
        cpo.chart_first_name = "lalala"

        cpo.chart_second_artist = "lalala1"
        cpo.chart_second_label = "lalala1"
        cpo.chart_second_name = "lalala1"

        cpo.chart_third_artist = "lalala2"
        cpo.chart_third_label = "lalala2"
        cpo.chart_third_name = "lalala2"

        cpo.publish_chart(chart_title)

    def test_add_release(self):
        self.login()
        release_name = "release title"
        # self.add_release(release_name)
        rpo = DiscographyPageObject(self.driver, self.base_url)

        rpo.edit_release_by_name(release_name)
        new_release_name = "new title forever"
        rpo.release_title = new_release_name
        rpo.publish_release(new_release_name)

    def add_release(self, release_name="release title" ):
        dpo = DiscographyPageObject(self.driver, self.base_url)

        dpo.add_release_btn_click()
        dpo.release_title = release_name
        dpo.release_artist = "artist"
        dpo.release_label = "label"
        dpo.release_date = "2013-03-27"

        dpo.select_genre()

        dpo.release_first_artist = "ar"
        dpo.release_first_track = "track"
        dpo.release_first_mix = "mix"
        dpo.release_first_hours = "0"
        dpo.release_first_minutes = "2"
        dpo.release_first_seconds = "33"

        dpo.release_second_artist = "ar"
        dpo.release_second_track = "track"
        dpo.release_second_mix = "mix"
        dpo.release_second_hours = "0"
        dpo.release_second_minutes = "2"
        dpo.release_second_seconds = "33"

        dpo.release_third_artist = "ar"
        dpo.release_third_track = "track"
        dpo.release_third_mix = "mix"
        dpo.release_third_hours = "0"
        dpo.release_third_minutes = "2"
        dpo.release_third_seconds = "33"

        dpo.publish_release(release_name)


    def test_add_new_entity(self):
        self.login()
        npo = PageNewsPageObject(self.driver, self.base_url)
        npo.add_news_btn_click()

        news_title = "temp title"
        npo.news_entry_title_element = news_title
        npo.news_entry_text_element = "ALALALALALALALHBAHHHH"
        npo.submit_news_entry(news_title)


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()