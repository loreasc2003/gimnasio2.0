from fastapi import APIRouter,Depends
import schemas, models
from cruds import crud
from sqlalchemy.orm import Session
from config.db import SessionLocal, engine

import schemas

user = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@user.get("/", tags=['Bienvenida'])

def bienvenida():
        return "Bienvenido al sistema de APIs"

@user.get("/users",response_model=list[schemas.users], tags=['Usuarios'])

def get_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
        users = crud.get_users(db, skip=skip, limit=limit)
        return users


# @user.post('/users', tags=['Usuarios'])

# def save_usuarios(insert_users:model_user):
#         users.append(insert_users)
#         #print (users)
#         return "Datos guardados"

# # BUSCAR
# @user.post('/users/', tags=['Usuarios'])
# def post_usuario(id: str):
#     for user in users:
#         if user.id == id:
#             return user
#     return {"error": "Usuario no encontrado"}

# #ACTUALIZAR
# @user.put('/users', tags=['Usuarios'])
# def update_usuario(id: str, updated_user: model_user):
#     for idx, user in enumerate(users):
#         if user.id == id:
#             users[idx] = updated_user
#             return "Datos actualizados"
#     return {"error": "Usuario no encontrado"}

# # ELIMINAR
# @user.delete('/users', tags=['Usuarios'])
# def delete_usuario(id: str):
#     for idx, user in enumerate(users):
#         if user.id == id:
#             del users[idx]
#             return "Usuario eliminado"
#     return {"error": "Usuario no encontrado"}