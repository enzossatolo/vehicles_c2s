from sqlalchemy import Column, Integer, String, Float

from src.database.db_conn import Base


class Vehicle(Base):
    __tablename__ = 'vehicles'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String)
    model = Column(String)
    year = Column(Integer)
    engine_type = Column(Float)
    fuel_type = Column(String)
    color = Column(String)
    mileage = Column(Float)
    doors_number = Column(Integer)
    transmission_type = Column(String)
    category = Column(String)
    price = Column(Float)
