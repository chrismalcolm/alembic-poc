from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, func


Base = declarative_base()
metadata = Base.metadata

class Counters(Base):
    __tablename__ = "counters"

    id = Column(Integer, primary_key=True)
    name = Column(String(60), unique=True, nullable=False)
    value = Column(Integer, default=0, nullable=False)
    created = Column(DateTime, default=func.now(), nullable=False)
    last_updated = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self):
        return f"id: {self.id}, name: {self.name} count: {self.value}"