import uuid
#Arquivo do backend responsável pela geração e renovação de tokens
#Tokens gerados conformes cadastro de novos usuários 
#Padrão Factory Pattern -> A criação de objetos deve ser isolada da lógica
class TokenFactory:
    def build_token(self, cpf):
        return f"{cpf}-{uuid.uuid4()}"
