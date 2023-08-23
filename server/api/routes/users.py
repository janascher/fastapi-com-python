from fastapi import APIRouter, status
from ..models.user import UserIn, UserOut
from ..services.users import UserManager
from ..controllers.users import PasswordManager

router = APIRouter()
user_manager = UserManager()
password_manager = PasswordManager()

# Rota para buscar a lista de usuários.
@router.get("/users", response_model=list[UserOut], status_code=status.HTTP_200_OK)
async def get_users():
    return user_manager.get_users()

# Rota para adicionar um novo usuário.
@router.post("/users", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def add_user(user: UserIn):
    hashed_password = password_manager.get_hashed_password(user.password)
    user.password = hashed_password
    return user_manager.add_user(user)

# Rota para atualizar os detalhes de um usuário existente.
@router.patch("/users/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: int, user: UserIn):
    return user_manager.update_user(user_id, user)

# Rota para deletar um usuário existente.
@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    return user_manager.delete_user(user_id)