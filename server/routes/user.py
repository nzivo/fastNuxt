from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User

user = APIRouter()

@user.get('/users')
def fetch_all():
    return conn.execute(users.select()).fetchall()

@user.post('/users')
def create_user(user: User):
    conn.execute(users.insert().values(name=user.name, email=user.email, password=user.password))
    return conn.execute(users.select()).fetchall()

@user.put('/users/{id}')
def update_user(user: User, id: int):
    conn.execute(users.update().values(name=user.name, email=user.email, password=user.password).where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()

@user.delete('/users/{id}')
def delete_user(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()