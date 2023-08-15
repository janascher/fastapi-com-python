from fastapi import APIRouter

# Criar uma instância do APIRouter
router = APIRouter()

# Definir um manipulador de solicitação para a rota raiz ("/") usando o decorador @app.get
@router.get("/")
def root():
    return{"message":"Hello World!!"}

