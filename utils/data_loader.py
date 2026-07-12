import json
import os
from models.config_model import Config
from models.user_model import User

class ConfigManager:
    _config: Config | None = None

    __CONFIG_PATH = os.path.join(os.path.dirname(__file__),"../config/config.json")

    @classmethod
    def load_config(cls) -> Config:
        if cls._config is None:
            with open(cls.__CONFIG_PATH) as file:
                data = json.load(file)
                cls._config = Config(**data)
        return cls._config

    @classmethod
    def get_config(cls) -> Config:
        return cls.load_config()

class TestDataLoader:

    __USERS_PATH = os.path.join(os.path.dirname(__file__),"../test_data/users.json")

    @classmethod
    def load_users(cls) -> list[User]:
        with open(cls.__USERS_PATH) as file:
            data = json.load(file)
            return [User(**user) for user in data]
