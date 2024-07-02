import models.persons
import schemas.persons
from sqlalchemy.orm import Session
import models, schemas

def get_person(db: Session, id:int):
    return db.query(models.persons.persons).filter(models.persons.persons.id== id).first()

def get_person_by_usuario(db: Session, nombre:str):
    return db.query(models.persons.persons).filter(models.persons.persons.nombre == nombre).first()

def get_users(db: Session, skip: int = 0, limit:int = 10):
    return db.query(models.persons.persons).offset(skip).limit(limit).all()

def create_person(db: Session, person: schemas.v.PersonCreate):
    db_person = models.persons.persons(nombre=person.nombre, primer_apellido=person.primer_apellido, segundo_apellido=person.segundo_apellido,direccion=person.direccion,telefono=person.telefono,correo=person.correo,created_at=person.created_at, estatus=person.estatus, Id_persona=person.Id_persona)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

def update_person(db: Session, id:int, person: schemas.persons.PersonUpdate):
    db_person = db.query(models.persons.persons).filter(models.persons.persons.id == id).first()
    if db_person:
        for var, value in vars(person).items():
            setattr(db_person, var, value) if value else None
        db.commit()
        db.refresh(db_person)
    return db_person

def delete_person(db: Session, id:int):
    db_person = db.query(models.persons.persons).filter(models.persons.persons.id == id).first()
    if db_person:
        db.delete(db_person)
        db.commit()
    return db_person