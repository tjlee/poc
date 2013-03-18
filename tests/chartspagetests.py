import unittest
from pageobjects.base.firefoxConnector import FirefoxConnector
from pageobjects.login.loginpageobject import LoginPageObject
from pageobjects.page.pagechartspageobject import PageChartsPageObject


class ChartsPageTests(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.driver = FirefoxConnector.driver
        self.driver.implicitly_wait(10)
        self.base_url = FirefoxConnector.base_url

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_add_new_chart(self):
        """
        Adds and removes created chart
        """
        self.login()
        chart_name = "test chart_name"
        self.add_chart(chart_name)
        self.remove_chart(chart_name)

    def test_edit_chart(self):
        """
        Adds chart -> edits chart -> removes chart
        """
        chart_name = "t2est2"
        new_chart_name = "t3est3"

        self.login()
        self.add_chart(chart_name)
        cpo = PageChartsPageObject(self.driver, self.base_url)

        cpo.edit_chart_by_name(chart_name)
        cpo.chart_title = new_chart_name
        cpo.publish_chart(new_chart_name)

        self.remove_chart(new_chart_name)

    def test_add_comment_to_chart(self):
        """
        Adds chart -> adds comment to the chart -> removes chart
        """
        chart_name = "t3est3"

        self.login()
        self.add_chart(chart_name)

        cpo = PageChartsPageObject(self.driver, self.base_url)
        cpo.comment_chart_by_name(comment="now way", chart_name=chart_name)

        self.remove_chart(chart_name)

    # def test_like_chart(self):
    #     #TODO

    # def test_import_from_sources(self):
    #     #TODO

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

    def remove_chart(self, chart_name="test chart name"):
        cpo = PageChartsPageObject(self.driver, self.base_url)
        cpo.delete_chart_by_name(chart_name)

    def login(self):
        lpo = LoginPageObject(self.driver, self.base_url)

        lpo.username = "tjlee@inbox.ru"
        lpo.password = "Welcome01@"
        lpo.submit()


if __name__ == "__main__":
    unittest.main()
