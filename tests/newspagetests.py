import unittest
import time
from pageobjects.login.loginpageobject import LoginPageObject
from pageobjects.page.pagenewspageobject import PageNewsPageObject
from pageobjects.base import selenium_driver


class NewsPageTests(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.driver = selenium_driver.connect()
        self.driver.implicitly_wait(10)
        self.base_url = selenium_driver.base_url

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_add_news_entity(self):
        news_title = "test_news tille"

        self.login()
        self.add_news_entity(news_title, "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam")
        self.remove_news_entity(news_title)

    def test_comment_news_entity(self):
        news_title = "title_to comment"

        self.login()
        self.add_news_entity(news_title, "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam")

        npo = PageNewsPageObject(self.driver, self.base_url)
        npo.comment_news_by_title(comment="to trolo lo lo", news_title=news_title)
        time.sleep(1) #hack as we slower than test :0
        self.remove_news_entity(news_title)

    def test_edit_news_entity(self):
        news_title = "test_news tille"
        new_news_title = "edited_title"

        self.login()
        self.add_news_entity(news_title=news_title)
        npo = PageNewsPageObject(self.driver, self.base_url)

        npo.edit_news_ty_title(news_title)
        npo.news_entry_title_element = new_news_title
        npo.submit_news_entry(new_news_title)

        self.remove_news_entity(new_news_title)

    def remove_news_entity(self, news_title):
        npo = PageNewsPageObject(self.driver, self.base_url)
        npo.delete_news_by_title(news_title)

    def add_news_entity(self, news_title="test", news_text="Lorem ipsum dolor"):
        npo = PageNewsPageObject(self.driver, self.base_url)

        npo.add_news_btn_click()
        npo.news_entry_title_element = news_title
        npo.news_entry_text_element = news_text

        npo.submit_news_entry(news_title)

    def login(self):
        lpo = LoginPageObject(self.driver, self.base_url)

        lpo.username = "tjlee@inbox.ru"
        lpo.password = "Welcome01@"
        lpo.submit()


if __name__ == "__main__":
    unittest.main()