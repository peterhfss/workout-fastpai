from src.models.entities.athletes import Athletes
from src.models.settings.database_connection_handler import DatabaseConnectionHandler
from sqlalchemy import insert

class AthleteRepository:
    async def add_athlete(self, athlete: dict) -> None:
        async with DatabaseConnectionHandler() as db:
            query = insert(Athletes).values(**athlete)
            await db.session.execute(query)
            await db.session.commit()
    