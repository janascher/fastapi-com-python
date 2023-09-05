from ..models.user import UserIn, UserOut
from ..controllers.users import PasswordManager

password_manager = PasswordManager()

class UserManager:
    def __init__(self):
        self.user_list = []
    
    # Obtém a lista de usuários atualmente armazenados.
    def get_users(self):
        return self.user_list

    # Adiciona um novo usuário à lista de usuários.
    def add_user(self, user: UserIn):
        hashed_password = password_manager.get_hashed_password(user.password)
        new_user = UserOut(
            id=user.id,
            name=user.name,
            email=user.email,
            password=hashed_password,
            avatar=user.avatar
        )
        self.user_list.append(new_user)
        
        return new_user

    # Atualiza os detalhes de um usuário existente.
    def update_user(self, user_id: int, user: UserIn):
        for index, existing_user in enumerate(self.user_list):
            if existing_user.id == user_id:
                user_with_hashed_password = UserOut(
                    id=user.id,
                    name=user.name,
                    email=user.email,
                    password=existing_user.password,
                    avatar=user.avatar
                )
                self.user_list[index] = user_with_hashed_password
                return {"message": "Usuário atualizado com sucesso"}
        return {"message": "Usuário não encontrado"}

    # Exclui um usuário existente.
    def delete_user(self, user_id: int):
        for index, user in enumerate(self.user_list):
            if user.id == user_id:
                del self.user_list[index]
                return {"message": "Usuário excluído com sucesso"}
        return {"message": "Usuário não encontrado"}
