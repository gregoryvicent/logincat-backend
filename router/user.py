from fastapi import APIRouter, Response
from config.db import engine
from model.user import users
from schema.user_schema import UserSchema
from cryptography.fernet import Fernet
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from typing import List

key = Fernet.generate_key()
crypt = Fernet(key)

user = APIRouter()


@user.get("/user", response_model=List[UserSchema])
def get_users():
    with engine.connect() as conn:
        result = conn.execute(users.select()).fetchall()

        return result


@user.get("/user/{id}", response_model=UserSchema)
def get_user(id: str):
    with engine.connect() as conn:
        result = conn.execute(users.select().where(users.c.id == id))

        return result.first()


@user.post("/user", status_code=HTTP_201_CREATED, response_model=UserSchema)
def create_user(data_user: UserSchema):
    with engine.connect() as conn:
        new_user = {"firstname": data_user.firstname,
                    "lastname": data_user.lastname}
        new_user["user_password"] = crypt.encrypt(data_user.user_password.encode("utf-8"))

        result = conn.execute(users.insert().values(new_user))

        return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


@user.put("/user/{id}", response_model=UserSchema)
def update_user(id: str, data_user: UserSchema):
    with engine.connect() as conn:
        conn.execute(users.update()
                          .values(
                              firstname=data_user.firstname, 
                              lastname=data_user.lastname, 
                              user_password=crypt.encrypt(data_user.user_password.encode("utf-8"))
                          )
                          .where(users.c.id == id))

        result = conn.execute(users.select().where(users.c.id == id))

        return result.first()


@user.delete("/user/{id}", status_code=HTTP_204_NO_CONTENT)
def delete_user(id: str):
    with engine.connect() as conn:
        conn.execute(users.delete().where(users.c.id == id))

        return Response(status_code=HTTP_204_NO_CONTENT)
