from sqlalchemy import Column, Integer, String, Text
from database import Base

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)

    service = Column(String)
    severity = Column(String)
    exception = Column(String)

    endpoint = Column(String)

    stack_trace = Column(Text)

    file_name = Column(String, nullable=True)

    line_number = Column(Integer, nullable=True)

    root_cause = Column(Text, nullable=True)

    status = Column(String, default="OPEN")