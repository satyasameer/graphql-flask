from .base import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime


class ModelMatches(Base):
    """Matches model."""

    __tablename__ = 'matches'

    id = Column('id', Integer, primary_key=True)
    match_name = Column('match_name', String(100))
    match_date = Column('match_date', DateTime)
    match_score = Column('match_score', String(50))
    match_status = Column('match_state', String(50))