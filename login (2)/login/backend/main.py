from fastapi import FastAPI
from services.auth_service import AuthService
#Arquivo principal (main) do backend / Registra rotas 
# Dispara conexão com o banco.
app = FastAPI()
auth_service = AuthService()

@app.post("/login")
def login(data: dict):
    cpf = data["cpf"]
    password = data["password"]
    return auth_service.login(cpf, password)
