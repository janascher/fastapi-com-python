from passlib.hash import bcrypt
from ...models.user import UserIn


class PasswordManager:
    
    @staticmethod
    # Retorna a versão criptografada (hash) da senha fornecida.
    def get_hashed_password(password: str) -> str:
        return bcrypt.hash(password)
    
    @staticmethod
    # Verifica se a senha fornecida corresponde à senha criptografada armazenada para o usuário.
    def verify_password(password: str, user: UserIn) -> bool:
        return bcrypt.verify(password, user.password)