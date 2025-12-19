from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import declarative_base
#Padrão DTO -> Funciona como entidade
#Funções que lidam com dados na camada de rotas agem como DTO'S
#Classe modelo que representa uma tabela do banco de dados 
#Definir estrutura de organização dos dados inseridos 
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    cpf = Column(String, primary_key=True)
    password = Column(String)
    active = Column(Boolean)
    role = Column(String)
