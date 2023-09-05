from pathlib import Path

from fastapi import APIRouter, Form, HTTPException, UploadFile, status

from ..controllers.users import PasswordManager
from ..models.user import UserIn, UserOut
from ..services.users import UserManager

router = APIRouter()
user_manager = UserManager()
password_manager = PasswordManager()

# Define o diretório onde os avatares serão armazenados
UPLOAD_DIR = "uploads"

# Verifica se o diretório de upload existe, se não, cria-o
Path(UPLOAD_DIR).mkdir(parents=True, exist_ok=True)

# Rota para buscar a lista de usuários.
@router.get("/users", response_model=list[UserOut], status_code=status.HTTP_200_OK)
async def get_users():
    return user_manager.get_users()

# Rota para adicionar um novo usuário.
@router.post("/users/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def add_user(
    id: int = Form(), 
    name: str = Form(),
    email: str = Form(),
    password: str = Form(),
    avatar: UploadFile = Form()
    ):

    # Verifica se o campo 'avatar' está presente na solicitação
    if not avatar:
        raise HTTPException(status_code=400, detail="O campo 'avatar' é obrigatório.")


    hashed_password = password_manager.get_hashed_password(password)

    try:
        # Salva o arquivo em um diretório
        file_path = f"uploads/{avatar.filename}"
        with open(file_path, "wb") as file:
            contents = await avatar.read()
            file.write(contents)
    except IOError:
        raise HTTPException(status_code=500, detail="Ocorreu um erro ao gravar o arquivo.")
    
    user_data = UserIn(
        id=id, 
        name=name,
        email=email,
        password=hashed_password,
        avatar=file_path
        )

    user = user_manager.add_user(user_data)

    return user

# Rota para atualizar os detalhes de um usuário existente.
@router.patch("/users/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: int, user: UserIn):
    return user_manager.update_user(user_id, user)

# Rota para deletar um usuário existente.
@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    return user_manager.delete_user(user_id)
