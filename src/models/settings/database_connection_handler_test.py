import pytest
from .database_connection_handler import DatabaseConnectionHandler

@pytest.mark.asyncio
@pytest.mark.skip(reason="Skipping database connection test")
async def test_connection():
    async with DatabaseConnectionHandler() as db:
        print(db.session)
        assert db.session is not None