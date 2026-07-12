import pytest
from loguru import logger
from driver import DriverSingleton
from utils.data_loader import ConfigManager

@pytest.fixture(scope="function", autouse=True)
def setup_teardown():
    logger.info("=" * 60)
    logger.info("Тест начат")
    logger.info("=" * 60)
    config = ConfigManager.get_config()
    DriverSingleton.get_driver().get(config.base_url)
    yield
    DriverSingleton.quit_driver()
    logger.info("=" * 60)
    logger.info("Тест завершен")
    logger.info("=" * 60)
