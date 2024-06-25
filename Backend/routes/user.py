from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

user = APIRouter()
users = []

#userModel esto iria en MODELS.py
class model_user(BaseModel):
        id:str
        usuario:str
        password: str
        created_at:datetime = datetime.now
        estatus:bool=False 

@user.get("/")

def bienvenida():
        return "Bienvenido al sistema de APIs"

@user.get("/users")

def get_usuarios():
        return users


@user.post('/users')

def save_usuarios(insert_users:model_user):
        users.append(insert_users)
        #print (users)
        return "Datos guardados"

@user.get('/users/')
def get_usuario(id: str):
    for user in users:
        if user.id == id:
            return user
    return {"error": "Usuario no encontrado"}

@user.put('/users')
def update_usuario(user_id: str, updated_user: model_user):
    for idx, user in enumerate(users):
        if user.id == id:
            users[idx] = updated_user
            return "Datos actualizados"
    return {"error": "Usuario no encontrado"}

@user.delete('/users')
def delete_usuario(id: str):
    for idx, user in enumerate(users):
        if user.id == id:
            del users[idx]
            return "Usuario eliminado"
    return {"error": "Usuario no encontrado"}