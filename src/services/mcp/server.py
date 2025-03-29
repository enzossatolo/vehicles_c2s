from mcp.server.fastmcp import FastMCP
from sqlalchemy import select
from src.database.db_conn import async_session
from src.models.vehicles import Vehicle
from src.config.config import logger

mcp = FastMCP("VehiclesServer")

@mcp.tool()
async def get_vehicle(
    brand: str = None,
    model: str = None,
    year_min: int = None,
    year_max: int = None,
    engine_type: str = None,
    fuel_type: str = None,
    color: str = None,
    mileage_min: float = None,
    mileage_max: float = None,
    doors_number: int = None,
    transmission_type: str = None,
    category: str = None,
    price_min: float = None,
    price_max: float = None
):
    """
    Retrieve vehicles from the database based on the provided filters.

    Parameters:
        brand (str, optional): The brand of the vehicle.
        model (str, optional): The model of the vehicle.
        year_min (int, optional): The minimum manufacturing year of the vehicle.
        year_max (int, optional): The maximum manufacturing year of the vehicle.
        engine_type (str, optional): The engine type or capacity of the vehicle.
        fuel_type (str, optional): The type of fuel used by the vehicle.
        color (str, optional): The color of the vehicle.
        mileage_min (float, optional): The minimum mileage of the vehicle.
        mileage_max (float, optional): The maximum mileage of the vehicle.
        doors_number (int, optional): The number of doors.
        transmission_type (str, optional): The transmission type of the vehicle.
        category (str, optional): The category of the vehicle.
        price_min (float, optional): The minimum price of the vehicle.
        price_max (float, optional): The maximum price of the vehicle.

    Returns:
        str: A formatted string containing the details of the vehicles that match the filters.
             If no vehicles are found, returns a message indicating no results.
    """
    async with async_session().begin() as session:
        query = select(Vehicle)

        if brand:
            query = query.where(Vehicle.brand.ilike(f"%{brand}%"))
        if model:
            query = query.where(Vehicle.model.ilike(f"%{model}%"))
        if year_min:
            query = query.where(Vehicle.year >= year_min)
        if year_max:
            query = query.where(Vehicle.year <= year_max)
        if engine_type:
            query = query.where(Vehicle.engine_type.ilike(f"%{engine_type}%"))
        if fuel_type:
            query = query.where(Vehicle.fuel_type.ilike(f"%{fuel_type}%"))
        if color:
            query = query.where(Vehicle.color.ilike(f"%{color}%"))
        if mileage_min:
            query = query.where(Vehicle.mileage >= mileage_min)
        if mileage_max:
            query = query.where(Vehicle.mileage <= mileage_max)
        if doors_number:
            query = query.where(Vehicle.doors_number == doors_number)
        if transmission_type:
            query = query.where(Vehicle.transmission_type.ilike(f"%{transmission_type}%"))
        if category:
            query = query.where(Vehicle.category.ilike(f"%{category}%"))
        if price_min:
            query = query.where(Vehicle.price >= price_min)
        if price_max:
            query = query.where(Vehicle.price <= price_max)

        results = [v[0] for v in (await session.execute(query)).all()]

    if not results:
        return "No vehicles found with the provided filters."

    response_lines = []
    for vehicle in results:
        line = (
            f"ID: {vehicle.id}, Brand: {vehicle.brand}, Model: {vehicle.model}, Year: {vehicle.year}, "
            f"Engine Type: {vehicle.engine_type}, Fuel Type: {vehicle.fuel_type}, "
            f"Color: {vehicle.color}, Mileage: {vehicle.mileage}, Doors: {vehicle.doors_number}, "
            f"Transmission: {vehicle.transmission_type}, Category: {vehicle.category}, Price: {vehicle.price}"
        )
        response_lines.append(line)
    response = "\n".join(response_lines)
    return response


if __name__ == "__main__":
    mcp.run()
