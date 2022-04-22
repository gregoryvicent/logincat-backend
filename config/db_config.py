from enum import Enum


class DataDB(Enum):
    DB_TYPE = "mysql+pymysql"
    DB_USER = "gregory"
    DB_PASSWORD = "12345"
    DB_HOST = "localhost"
    DB_PORT = "3306"
    DB_NAME = "logincat"
