from selenium import webdriver


class SeleniumWrapper:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SeleniumWrapper, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def connect(self, host="https://dev.labbler.com/"):
        # TODO: change driver by parameter
        self.driver = webdriver.Firefox()
        self.base_url = host
        return self.driver