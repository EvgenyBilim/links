from fastapi import APIRouter, Depends
from app.db.links import DBLinks
from deps.db import get_db_depend
from deps.links import get_link_depend
from domain.link_shortener import LinkShortener
from schemas.links import LinkResponse, LinkDeleted

router = APIRouter()


@router.put("/create_short_url")
async def create_short_url(
    long_url: str,
    link_shortener=Depends(get_link_depend(LinkShortener)),
    db_links=Depends(get_db_depend(DBLinks))
) -> LinkResponse:
    """Создание короткой ссылки."""

    # 1. Сократить ссылку
    short_url = link_shortener.short(long_url)

    # 2. Записать ссылку в бд
    link_pk = await db_links.create(long_url, short_url)

    # 3. Вернуть ссылку в ответе
    response = LinkResponse.model_validate(
        {
            "pk": link_pk,
            "long_url": long_url,
            "short_url": short_url,
        }
    )
    return response


@router.delete("/delete_url")
async def delete_url(
    short_url: str,
    db_links=Depends(get_db_depend(DBLinks))
) -> LinkDeleted:
    """Удаление ссылки."""

    status = await db_links.delete(short_url)
    response = LinkDeleted.model_validate(status)

    return response


@router.get("/get_full_url")
async def get_full_url(
    short_url: str,
    db_links=Depends(get_db_depend(DBLinks))
) -> LinkResponse:
    """Получение полного url."""

    link_data = await db_links.get(short_url)
    response = LinkResponse.model_validate(link_data)

    return response
