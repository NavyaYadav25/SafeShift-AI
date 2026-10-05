from sqlalchemy import Column, Integer, String
from database import Base


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)

    service = Column(String)
    severity = Column(String)
    exception = Column(String)
    endpoint = Column(String)
    stack_trace = Column(String)

    status = Column(String, default="OPEN")

    root_cause = Column(String)

    severity_score = Column(Integer)

    fix_suggestion = Column(String)