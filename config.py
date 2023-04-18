import os

from dotenv import load_dotenv

load_dotenv()


class Config():
    """Global configuration module"""
    SERVER_NAME_ONE = os.getenv("hostdb")
    DEBUG = True