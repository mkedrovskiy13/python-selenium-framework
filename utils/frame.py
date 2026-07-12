from loguru import logger
from selenium.webdriver.support.wait import WebDriverWait
from driver import DriverSingleton
from selenium.webdriver.support import expected_conditions as EC
from utils.data_loader import ConfigManager

class Frame():

    @staticmethod
    def switch_to_frame(locator):
        logger.info("Переключаемся на фрейм")
        WebDriverWait(DriverSingleton.get_driver(), ConfigManager.get_config().timeout).until(EC.frame_to_be_available_and_switch_to_it(locator))
