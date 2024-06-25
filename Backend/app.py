from fastapi import FastAPI
from routes.user import user
from routes.person import person

app=FastAPI()
app.include_router(user)
app.include_router(person)

print ("por que tan coqueta Angelita????")


# models.py

