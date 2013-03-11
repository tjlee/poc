import unittest
import time


class BasePageObject(unittest.TestCase):
    def wait_for_element_displayed_by_id(self, driver, locator, timeout=60, msg="[error] element is not found" ):
        for i in range(timeout):
            try:
                if driver.find_element_by_id(locator).is_displayed(): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail(msg)

    def wait_for_element_displayed_by_css(self, driver, locator, timeout=60, msg="[error] element is not found" ):
        for i in range(timeout):
            try:
                if driver.find_element_by_css_selector(locator).is_displayed(): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail(msg)

    def wait_for_css_selection_text(self, driver, locator, text, timeout=5, msg="[error]: statistic is not shown"):
        for i in range(timeout):
            try:
                if driver.find_element_by_css_selector(locator).text == text: break
            except:
                pass
            time.sleep(1)
        else:
            self.fail(msg)

    def wait_for_element_displayed_by_class(self, driver, locator, timeout=60, msg="[error] element is not found" ):
        for i in range(timeout):
            try:
                if driver.find_element_by_class_name(locator).is_displayed(): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail(msg)

    def wait_for_element_displayed_by_multiple_classes(self, driver, locator1, locator2, timeout=60,
                                                       msg="[error] element is not found" ):
        for i in range(timeout):
            try:
                if driver.find_element_by_class_name(locator1).is_displayed() or \
                        driver.find_element_by_class_name(locator2): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail(msg)

    def wait_for_page_title(self, driver, title, timeout=60, msg="[error] title is not correct"):
        for i in range(60):
            try:
                if driver.title == title: break
            except:
                pass
            time.sleep(1)
        else:
            self.fail(msg)
