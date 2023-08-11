from fastapi import FastAPI

# Criar uma instância do aplicativo FastAPI
app = FastAPI()

# Definir um manipulador de solicitação para a rota raiz ("/") usando o decorador @app.get
@app.get("/")
def root():
    return{"message":"Hello World!!"}