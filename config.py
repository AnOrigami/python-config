import os
from dotenv import load_dotenv, find_dotenv

from typing import List

from pydantic.v1 import BaseSettings


class Config(BaseSettings):
    LISTEN = 8000
    REDIS = 'redis://192.168.17.131:6379/2'
    MONGO = 'mongodb://192.168.17.131:27017/desensitization_platform'


settings = Config()
