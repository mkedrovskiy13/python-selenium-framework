from loguru import logger
from elements.base_element import BaseElement
class TextField(BaseElement):

    def enter_text(self, value):
        logger.info("текст введен")
        self._find().send_keys(value)
