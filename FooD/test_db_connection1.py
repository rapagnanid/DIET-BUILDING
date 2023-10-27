from models import Base
from sqlalchemy import create_engine

# Configura il URL del database
engine = create_engine('mysql://root:Cocodemer.95@localhost/FooD')  # Assicurati che il nome del database corrisponda

# Crea le tabelle
Base.metadata.create_all(engine)