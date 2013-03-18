from pageobjects.base.firefoxConnector import FirefoxConnector


class BasePageElement(object):
    def __get__(self, obj, cls=None):
        FirefoxConnector.driver.name

    def __delete__(self, obj):
        pass