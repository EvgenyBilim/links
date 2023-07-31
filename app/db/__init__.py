from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.pool import QueuePool

from app.config import DB_URL


Base = declarative_base()

engine: AsyncEngine = create_async_engine(
    DB_URL, poolclass=QueuePool, echo=False,
)

Session: async_sessionmaker[AsyncSession] = async_sessionmaker(
    engine, expire_on_commit=False, autocommit=False, autoflush=False
)
