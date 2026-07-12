from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver import DriverSingleton
from utils.data_loader import ConfigManager

class Waiting:

    @staticmethod
    def _get_wait():
        driver = DriverSingleton.get_driver()
        timeout = ConfigManager.get_config().timeout
        return WebDriverWait(driver, timeout)

    @staticmethod
    def wait_for_alert():
        return Waiting._get_wait().until(EC.alert_is_present())

    @staticmethod
    def wait_for_presence(locator):
        return Waiting._get_wait().until(EC.presence_of_element_located(locator))

    @staticmethod
    def wait_for_visible(locator):
        return Waiting._get_wait().until(EC.visibility_of_element_located(locator))

    @staticmethod
    def wait_for_clickable(locator):
        return Waiting._get_wait().until(EC.element_to_be_clickable(locator))

    @staticmethod
    def wait_for_text(locator):
        return Waiting._get_wait().until(lambda driver: driver.find_element(*locator).text.strip() != "")
