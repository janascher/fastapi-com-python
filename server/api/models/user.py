from pydantic import BaseModel, SecretStr

# Define o esquema de entrada (input) para os dados do usuário.
class UserIn(BaseModel):
    id: int
    name: str
    email: str
    password: str

# Define o esquema de saída (output) para os dados do usuário.
class UserOut(BaseModel):
    id: int
    name: str
    email: str
    password: SecretStr
