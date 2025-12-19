from abc import ABC, abstractmethod
#Padrão de projeto Strategy / Usado para autenticação de usuários 
#Senha / Token / Biometria "self , user , pass"
class AuthStrategy(ABC):
    @abstractmethod
    def authenticate(self, user, password):
        pass

class PasswordStrategy(AuthStrategy):
    def authenticate(self, user, password):
        return user and user.password == password
