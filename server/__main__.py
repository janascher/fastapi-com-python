from api.routes import Home, users
from configs import ALLOWED_ORIGINS, HOST, PORT
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run


class APIServer:
    def __init__(self):
        self.app = FastAPI()

    # Configura a política de CORS (Cross-Origin Resource Sharing) para o servidor.
    def configure_cors(self, origins):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    # Inclui os roteadores (routers) da API no servidor.
    def include_routers(self):
        self.app.include_router(Home.router)
        self.app.include_router(users.router)

    # Inicia o servidor FastAPI.
    def run_server(self, host, port):
        run(self.app, host=host, port=port)

if __name__ == "__main__":
    api_server = APIServer()
    api_server.configure_cors(ALLOWED_ORIGINS)
    api_server.include_routers()
    api_server.run_server(HOST, PORT)
