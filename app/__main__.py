from uvicorn import run
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.server.routes import Users, Home
from api.configs import HOST, PORT, ALLOWED_ORIGINS

# Criar uma instância da FastAPI
app = FastAPI()

# Configurar o CORS
origins = ALLOWED_ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir os roteadores na aplicação FastAPI
app.include_router(Home.router)
app.include_router(Users.router)

if __name__ == "__main__":
    # Iniciar o servidor UVicorn utilizando a instância 'app', especificando o host e a porta
    run(app, host=HOST, port=PORT)
