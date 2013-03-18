import unittest
from pageobjects.base import selenium_driver
from pageobjects.login.loginpageobject import LoginPageObject
from pageobjects.page.discographypageobject import DiscographyPageObject


class DiscographyPageTests(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.driver = selenium_driver.connect()
        self.driver.implicitly_wait(10)
        self.base_url = selenium_driver.base_url

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_add_new_release(self):
        self.login()
        release_name = "release title"
        self.add_release(release_name)
        self.remove_release(release_name)

    def test_edit_release(self):
        release_name = "release_title"
        new_release_name = "new title_forever"

        self.login()
        self.add_release(release_name)
        rpo = DiscographyPageObject(self.driver, self.base_url)

        rpo.edit_release_by_name(release_name)
        rpo.release_title = new_release_name
        rpo.publish_release(new_release_name)

        self.remove_release(new_release_name)

    def test_comment_release_by_name(self):
        release_name = "new title forever3"
        self.login()
        self.add_release(release_name)

        dpo = DiscographyPageObject(self.driver, self.base_url)
        dpo.comment_release_by_name(comment="to to ro bo", release_name=release_name)

        self.remove_release(release_name)

    def add_release(self, release_name="release title"):
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

    def remove_release(self, release_name = "release title"):
        rpo = DiscographyPageObject(self.driver, self.base_url)
        rpo.delete_release_by_name(release_name)

    def login(self):
        lpo = LoginPageObject(self.driver, self.base_url)

        lpo.username = "tjlee@inbox.ru"
        lpo.password = "Welcome01@"
        lpo.submit()


if __name__ == "__main__":
    unittest.main()