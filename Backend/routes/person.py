from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

person = APIRouter()
persons = []

#userModel esto iria en MODELS.py
class model_person(BaseModel):
        id:str
        nombre:str
        primer_apellido: str
        segundo_apellido: str
        direccion: str
        telefono: str
        correo: str
        sangre: str
        fecha_nacimiento: datetime
        created_at:datetime = datetime.now()
        estatus:bool=False 

@person.get("/", tags=['Bienvenida'])

def bienvenida():
        return "Bienvenido al sistema de APIs"

@person.get("/person", tags=['Personas'])
def get_person():
        return persons


@person.post("/person", tags=['Personas'])
def save_person(insert_person:model_person):
        persons.append(insert_person)
        #print (users)
        return "Datos guardados"

# BUSCAR
@person.post('/person/', tags=['Personas'])
def post_person(id: str):
    for person in persons:
        if person.id == id:
            return person
    return {"error": "Persona no encontrada"}

#ACTUALIZAR
@person.put('/person', tags=['Personas'])
def update_person(id: str, updated_person: model_person):
    for idx, person in enumerate(persons):
        if person.id == id:
            persons[idx] = updated_person
            return "Datos actualizados"
    return {"error": "Usuario no encontrado"}

# ELIMINAR
@person.delete('/person', tags=['Personas'])
def delete_person(id: str):
    for idx, person in enumerate(persons):
        if person.id == id:
            del persons[idx]
            return "Usuario eliminado"
    return {"error": "Usuario no encontrado"}