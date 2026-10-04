from fastapi import FastAPI
from sqlalchemy.orm import Session

from database import engine
from database import SessionLocal

from models import Base
from models import Incident

from schemas import IncidentCreate
from investigator import investigate_incident

app = FastAPI(title="SafeShift AI")

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "SafeShift AI Running"
    }


@app.post("/incident")
def create_incident(data: IncidentCreate):

    db: Session = SessionLocal()

    analysis = investigate_incident(
        data.exception,
        data.stack_trace
    )

    incident = Incident(
        service=data.service,
        severity=data.severity,
        exception=data.exception,
        endpoint=data.endpoint,
        stack_trace=data.stack_trace,
        root_cause=analysis["root_cause"]
    )

    db.add(incident)
    db.commit()
    db.refresh(incident)

    return {
        "incident_id": incident.id,
        "status": "created"
    }


@app.get("/incidents")
def get_incidents():

    db: Session = SessionLocal()

    incidents = db.query(Incident).all()

    return incidents