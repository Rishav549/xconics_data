from sqlalchemy.orm import Session
from sqlalchemy import desc
from models.data import DataPacket
import datetime
from datetime import timedelta, timezone
import re

def create_data_packet(db: Session, data: str):
    data_packet = DataPacket(data=data, created_at=utc_to_ist(datetime.datetime.utcnow()))
    db.add(data_packet)
    db.commit()
    db.refresh(data_packet)
    return data_packet

def utc_to_ist(utc_time: datetime.datetime) -> datetime.datetime:
    ist_time = utc_time + timedelta(hours=5, minutes=30)
    return ist_time