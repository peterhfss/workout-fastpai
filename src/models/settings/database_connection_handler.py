from sqlalchemy.ext.asyncio import  create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from typing import Optional

CONNECTION_STRING = "postgresql+asyncpg://postgres:1234@localhost:5432/postgres"

engine = create_async_engine(
    CONNECTION_STRING,
    echo=False,
    pool_size=2,
    max_overflow=0,
    pool_timeout=30
)

async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

class DatabaseConnectionHandler:
    def __init__(self) -> None:
        self.session: Optional[AsyncSession] = None

    async def __aenter__(self):
        self.session = async_session()
        return self

    async def __aexit__(self, exc_type, exc_value, exc_tb):
        await self.session.close()