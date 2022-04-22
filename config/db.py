from sqlalchemy import create_engine, MetaData
from config.db_config import DataDB


db_type = DataDB.DB_TYPE.value
db_user = DataDB.DB_USER.value
db_password = DataDB.DB_PASSWORD.value
db_host = DataDB.DB_HOST.value
db_port = DataDB.DB_PORT.value
db_name = DataDB.DB_NAME.value


engine = create_engine(f"{db_type}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

meta_data = MetaData()