from typing import Annotated, AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import Session


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with Session() as session:
        yield session


def get_db_depend(obj):
    def func(session: Annotated[AsyncSession, Depends(get_session)]):
        return obj(session)

    return func
