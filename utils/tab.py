from loguru import logger
from driver import DriverSingleton

class Tab():

    @staticmethod
    def switch_to_new_tab():
        logger.info("переключились на новую вкладку")
        handles = DriverSingleton.get_driver().window_handles
        DriverSingleton.get_driver().switch_to.window(handles[-1])

    @staticmethod
    def switch_to_tab(handle):
        logger.info("переключились на прошлую вкладку")
        DriverSingleton.get_driver().switch_to.window(handle)

    @staticmethod
    def close_current_tab():
        logger.info("закрыли вкладку")
        DriverSingleton.get_driver().close()
