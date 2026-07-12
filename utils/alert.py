from loguru import logger
from driver import DriverSingleton
from utils.waiting import Waiting

class Alert:

    @staticmethod
    def enter_text(text: str):
        logger.info("текст введен")
        Waiting.wait_for_alert().send_keys(text)

    @staticmethod
    def is_closed():
        try:
            alert = DriverSingleton.get_driver().switch_to.alert
            logger.info("Алерт не закрыт")
            return False
        except:
            logger.info("Алерт закрыт")
            return True

    @staticmethod
    def accept():
        Waiting.wait_for_alert().accept()
        logger.info("Нажата кнопка ОК")

    @staticmethod
    def get_text():
        logger.info("Получили текст из алерта")
        return Waiting.wait_for_alert().text
