from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils.data_loader import ConfigManager

class BrowserFactory:

    @staticmethod
    def create_driver(browser_name):
        config = ConfigManager.get_config()
        browser_name = browser_name.lower().strip()

        if browser_name == "chrome":
            options = ChromeOptions()
            if config.incognito:
                options.add_argument("--incognito")
            if config.maximized:
                options.add_argument("--start-maximized")
            options.page_load_strategy = config.page_load_strategy
            return webdriver.Chrome(options=options)

        elif browser_name == "firefox":
            options = FirefoxOptions()
            if config.incognito:
                options.set_preference("browser.privatebrowsing.autostart", True)
            options.page_load_strategy = config.page_load_strategy

            driver = webdriver.Firefox(options=options)
            if config.maximized:
                driver.maximize_window()
            return driver

        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
