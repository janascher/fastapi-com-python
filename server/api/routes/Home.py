from fastapi import APIRouter

# Classe responsável por lidar com as requisições para a rota raiz ("/").
class HomeHandler:
    # Retorna um dicionário contendo uma mensagem de saudação.
    def root(self):
        return {"message": "Hello World!!"}

home_handler = HomeHandler()
router = APIRouter()
router.get("/", response_model=dict)(home_handler.root)
