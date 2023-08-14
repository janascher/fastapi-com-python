from fastapi import FastAPI
from pydantic import BaseModel

# Criar uma instância do aplicativo FastAPI
app = FastAPI()

# Definir o modelo de dados dos usuários
class Users(BaseModel):
    name: str
    password: str
    email: str

# Definir uma lista de usuários mocados (valores pré-definidos)
users = [
        Users(name="Joana", password="123", email="joana@email.com"),
        Users(name="Felipe", password="456", email="felipe@email.com")
    ]

# Definir o endpoint GET "/users" para retornar a lista de usuários
@app.get("/users", response_model=list[Users])
def get_users():
    return users
