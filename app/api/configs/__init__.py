from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

# Definir as variáveis de ambiente
HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))  # Converte a variável PORT para um número inteiro
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS").split(",")  # Obter as origens permitidas do ambiente