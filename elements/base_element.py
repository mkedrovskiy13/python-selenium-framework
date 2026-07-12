from abc import ABC
from loguru import logger
from utils.waiting import Waiting
class BaseElement(ABC):

    def __init__(self, locator, name):
        self.locator = locator
        self.name = name

    def _find(self):
        logger.info(f"Найден элемент: {self.name}")
        return Waiting.wait_for_presence(self.locator)

    def is_present(self):
        try:
            logger.info(f"Проверка, что элемент существует: {self.name}")
            self._find()
            return True
        except:
            return False

    def _wait_for_visible(self):
        logger.info(f"Ожидание видимости элемента: {self.name}")
        return Waiting.wait_for_visible(self.locator)

    def is_visible(self):
        try:
            self._wait_for_visible()
            logger.info(f"Проверка, что элемент видимый: {self.name}")
            return True
        except:
            return False

    def _wait_for_clickable(self):
        logger.info(f"Ожидание кликабельности элемента: {self.name}")
        return Waiting.wait_for_clickable(self.locator)

    def is_clickable(self):
        try:
            self._wait_for_clickable()
            logger.info(f"Проверка элемента на кликабельность: {self.name}")
            return True
        except:
            return False

    def click(self):
        element = self._wait_for_clickable()
        logger.info(f"Нажат элемент: {self.name}")
        element.click()

    def get_text(self):
        logger.info(f"Получен текст элемента: {self.name}")
        return self._find().text
