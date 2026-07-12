from browser_factory import BrowserFactory
from utils.data_loader import ConfigManager

class DriverSingleton:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            config = ConfigManager.get_config()
            browser_name = config.browser
            cls._driver = BrowserFactory.create_driver(browser_name)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
