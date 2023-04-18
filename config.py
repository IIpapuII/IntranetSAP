import os

from dotenv import load_dotenv

load_dotenv()


class Config():
    """Global configuration module"""
    SERVER_NAME_ONE = os.getenv("hostdb")
    DATABASE_ONE = os.getenv("database")
    USERDB_ONE = os.getenv("userDB")
    PASSWOR_One= os.getenv("passwordDB")

    SERVER_SAP = os.getenv("SERVERSAP")
    USER_SAP = os.getenv("USERSAP")
    PASSWORD_SAP = os.getenv("PASSWORD_SAP")
    PORT_SAP = os.getenv("PORTSAP")
    USER_MAIL = os.getenv("USERMAIL")
    PASSWORD_MAIL = os.getenv("PASSWORDEMAIL")
    DEBUG = True

    TEMPLATE_FOLDER = "views/templates/"
    STATIC_FOLDER = "views/static"