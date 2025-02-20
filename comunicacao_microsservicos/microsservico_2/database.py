from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Cria a engine do SQLAlchemy, conectando-se ao banco de dados via URL definida nas variáveis de ambiente
engine = create_engine(os.environ["DATABASE_URL_MICROSSERVICO_2"])

# Configura a sessão do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define a classe base para os modelos do SQLAlchemy
Base = declarative_base()

# Cria a tabela no banco de dados se ela ainda não existir
Base.metadata.create_all(bind=engine)

def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
