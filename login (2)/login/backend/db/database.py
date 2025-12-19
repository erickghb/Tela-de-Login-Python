from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#Camada responsável pela conexão com o banco de dados. 
# Melhora a organização evitando repetição de código em outras camadas.
#Padrão Separations of Concerns 

class Database:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            engine = create_engine("postgresql://user:pass@localhost/login")
            cls._instance = sessionmaker(bind=engine)()
        return cls._instance
