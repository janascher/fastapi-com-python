from uvicorn import run
from api.server import app
from api.configs import HOST, PORT

if __name__ == "__main__":
    # Iniciar o servidor UVicorn utilizando a instância 'app', especificando o host e a porta
    run(app, host=HOST, port=PORT)
