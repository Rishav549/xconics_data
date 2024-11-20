from sqlalchemy import Column, Integer, Float, Text, DateTime, String
from db.db import Base
import datetime

class DataPacket(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(String , index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)