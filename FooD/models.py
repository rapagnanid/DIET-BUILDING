from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class NutritionalData(Base):
    __tablename__ = 'nutritional_data'

    id = Column(Integer, primary_key=True)
    food_name = Column(String(255))  # Sostituisci 255 con la lunghezza desiderata
    nutrient_name = Column(String(255))  # Sostituisci 255 con la lunghezza desiderata
    nutrient_value = Column(Float)
    unit_name = Column(String(255))  # Sostituisci 255 con la lunghezza desiderata

