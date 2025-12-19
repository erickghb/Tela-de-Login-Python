from repositories.user_repository import UserRepository
from factories.token_factory import TokenFactory
from services.auth_strategy import PasswordStrategy
#Validação de login / Criação de usuários / Geração de tokens 
#Regras de autenticação definidos na função de "buscar CPF"
#Caso busque e esteja divergente, retorna "Error"
#Padrão Service Layer Pattern - > separação da camada de rotas
   
class AuthService:
    def __init__(self):
        self.repository = UserRepository()
        self.strategy = PasswordStrategy()
        self.factory = TokenFactory()

    def login(self, cpf, password):
        user = self.repository.find_by_cpf(cpf)

        if not self.strategy.authenticate(user, password):
            return {"error": "Credenciais inválidas"}

        token = self.factory.build_token(cpf)

        return {
            "message": "Login realizado",
            "token": token,
            "role": user.role
        }
