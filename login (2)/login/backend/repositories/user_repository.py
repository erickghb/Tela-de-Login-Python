from db.database import Database
from models.user import User
#Camada de acesso aos dados (conforme função de request --database--)
#Cria usuário / Busca e-mail / Valida login / Atualiza os tokens gerados
#Padrão Repository Pattern -> isola o acesso ao banco de dados
class UserRepository:
    def __init__(self):
        self.db = Database()

    def find_by_cpf(self, cpf):
        return self.db.query(User).filter(User.cpf == cpf).first()
