from loguru import logger
from driver import DriverSingleton
from elements.base_element import BaseElement

class WebTable(BaseElement):

    def get_rows(self):
        logger.info("получили строки")
        return DriverSingleton.get_driver().find_elements(*self.locator)
