from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import String, Integer
from config.db import meta_data, engine

users = Table("users", meta_data, 
            Column("id", Integer, primary_key=True), 
            Column("firstname", String(255), nullable=False),
            Column("lastname", String(255), nullable=False),
            Column("user_password", String(255), nullable=False))

meta_data.create_all(engine)