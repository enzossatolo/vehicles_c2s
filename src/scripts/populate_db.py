import asyncio
import random

from src.config.config import logger
from src.database.db_conn import async_session, Base, get_db_engine
from src.models.vehicles import Vehicle


async def populate_db():
    brands = ["Toyota", "Ford", "Chevrolet", "Honda", "Fiat", "Volkswagen", "Hyundai", "Nissan", "Kia", "BMW"]
    models = ["Corolla", "Fiesta", "Onix", "Civic", "Uno", "Gol", "HB20", "March", "Sportage", "320i"]
    fuel_types = ["Gasoline", "Alcohol", "Flex", "Diesel", "Electric"]
    transmissions = ["Manual", "Automatic"]
    categories = ["Sedan", "SUV", "Hatch", "Pickup", "Convertible", "Minivan"]
    colors = ["Black", "White", "Red", "Silver", "Blue", "Gray"]
    async with async_session().begin() as session:
        for _ in range(100):
            vehicle = Vehicle(
                brand=random.choice(brands),
                model=random.choice(models),
                year=random.randint(2000, 2025),
                engine_type=round(random.uniform(1.0, 2.0), 1),
                fuel_type=random.choice(fuel_types),
                color=random.choice(colors),
                mileage=round(random.uniform(0, 200000), 1),
                doors_number=random.choice([2, 4]),
                transmission_type=random.choice(transmissions),
                category=random.choice(categories),
                price=round(random.uniform(5000, 500000), 2)
            )
            session.add(vehicle)
    logger.info("Database populated with 100 vehicle records.")


def create_all_tables():
    engine = get_db_engine()
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_all_tables()
    asyncio.run(populate_db())
