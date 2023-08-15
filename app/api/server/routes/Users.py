from fastapi import APIRouter, status
from pydantic import BaseModel

# Criar uma instância do APIRouter
router = APIRouter()

# Definir o modelo de dados dos usuários
class Users(BaseModel):
    id: int
    name: str
    password: str
    email: str

# Criar uma lista vazia para armazenar os dados do usuário na memória
user_list = []

# Definir o endpoint GET "/users" para retornar a lista de usuários
@router.get("/users", response_model=list[Users], status_code=status.HTTP_200_OK)
def get_users():
    return user_list

# Definir o endpoint POST "/users" para retornar a lista de usuários
@router.post("/users", response_model=Users, status_code=status.HTTP_201_CREATED)
def add_user(users: Users):
    """
        Para testar no Postman:
            {
                "id": 1,
                "name": "Joana",
                "password": "123",
                "email": "joana@email.com"
            }

    """
    # Adicionar o usuário para a lista na memória
    user_list.append(users)
    return users

# Definir o endpoint PATCH "/users" para retornar a lista de usuários
@router.patch("/users/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: int, users: Users):
    """
        Para testar no Postman:
            {
                "id": 1,
                "name": "Novo nome do usuário",
                "password": "nova senha",
                "email": "novoemail@email.com"
            }

    """
    for index, existing_user in enumerate(user_list):
        if existing_user.id == user_id:
            user_list[index] = users
            return users
    return {"message": "Usuário não encontrado"}

# Definir o endpoint DELETE "/users" para retornar a lista de usuários
@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    for index, user in enumerate(user_list):
        if user.id == user_id:
            del user_list[index]
            return
    return {"message": "Usuário não encontrado"}

