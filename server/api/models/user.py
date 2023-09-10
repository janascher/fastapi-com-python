from pydantic import BaseModel, SecretStr
from typing import Dict, Any


# Define o esquema de entrada (input) para os dados do usuário.
class UserIn(BaseModel):
    id: int
    name: str
    email: str
    password: str
    avatar: str

# Define o esquema de saída (output) para os dados do usuário.
class UserOut(BaseModel):
    id: int
    name: str
    email: str
    password: SecretStr
    avatar: str

    def serialize(self) -> Dict[str, Any]:
        # Converte o campo SecretStr para uma string antes da serialização
        user_dict = {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "avatar": self.avatar
        }
        return user_dict
