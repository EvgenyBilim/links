from app.models.links import Links
from sqlalchemy import delete, select


class DBLinks:

    def __init__(self, session):
        self.session = session

    async def _get(self, pk=None, long_url=None, short_url=None):
        query = select(Links)

        if pk is not None:
            query = query.filter(Links.pk == pk)
        if long_url is not None:
            query = query.filter(Links.long_url == long_url)
        if short_url is not None:
            query = query.filter(Links.short_url == short_url)

        return (await self.session.execute(query)).scalars()

    async def get(self, short_url: str) -> dict:
        records = await self._get(short_url=short_url)
        if record := records.first():
            return {
                "pk": record.pk,
                "long_url": record.long_url,
                "short_url": record.short_url,
            }
        return {}

    async def create(self, long_url, short_url) -> int:
        records = await self._get(long_url=long_url)

        if record := records.first():
            print(f"Link with pk={record.pk} is already exists")
            return record.pk
        else:
            new_link = Links(
                long_url=long_url,
                short_url=short_url,
            )
            self.session.add(new_link)
            await self.session.commit()
            return new_link.pk

    async def delete(self, short_url: str) -> dict:
        try:
            query = delete(Links).where(Links.short_url == short_url)
            await self.session.execute(query)
            await self.session.commit()
            return {"status": "delete"}
        except Exception:
            return {"status": "error"}
