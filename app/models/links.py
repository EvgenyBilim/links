from app.db import Base
from sqlalchemy import Column, Integer, String, Identity


class Links(Base):
    __tablename__ = "links"

    pk = Column(Integer, Identity(), primary_key=True)
    long_url = Column(String, nullable=False)
    short_url = Column(String, nullable=False)
