from pydantic import BaseModel


class LinkResponse(BaseModel):
    pk: int
    long_url: str
    short_url: str


class LinkDeleted(BaseModel):
    status: str
