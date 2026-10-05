from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from datetime import datetime
import random

from database import engine
from database import SessionLocal

from models import Base
from models import Incident

from schemas import IncidentCreate

from investigator_agent import investigate_incident

from agents.investigator import investigate
from agents.diagnosis import diagnose
from agents.fixer import generate_fix
from agents.approval import approval_status

from business_impact import calculate_business_impact
from recovery_plan import generate_recovery_plan
from code_fixes import generate_code_fix
from risk_assessment import assess_risk
from agent_activity import get_agent_activity
from metrics import calculate_metrics
from timeline_store import timeline_events
from deployment_simulator import simulate_deployment
from agent_reasoning import generate_reasoning

app = FastAPI(title="SafeShift AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://safeshift-ai-frontend.onrender.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "SafeShift AI Running"
    }


@app.post("/incident")
def create_incident(data: IncidentCreate):

    db: Session = SessionLocal()

    try:
        analysis = investigate_incident(
            data.exception,
            data.stack_trace
        )

        current_time = datetime.now().strftime("%H:%M:%S")

        timeline_events.append(
            {
                "time": current_time,
                "event": f"Alert Triggered - {data.service}"
            }
        )

        timeline_events.append(
            {
                "time": current_time,
                "event": "Investigator Agent Started"
            }
        )

        timeline_events.append(
            {
                "time": current_time,
                "event": "Root Cause Identified"
            }
        )

        timeline_events.append(
            {
                "time": current_time,
                "event": "Recovery Plan Generated"
            }
        )

        timeline_events.append(
            {
                "time": current_time,
                "event": "Awaiting Human Approval"
            }
        )

        incident = Incident(
            service=data.service,
            severity=data.severity,
            exception=data.exception,
            endpoint=data.endpoint,
            stack_trace=data.stack_trace,
            root_cause=analysis["root_cause"],
            severity_score=analysis["severity_score"],
            fix_suggestion=analysis["fix_suggestion"]
        )

        db.add(incident)
        db.commit()
        db.refresh(incident)

        return {
            "incident_id": incident.id,
            "status": "created"
        }

    finally:
        db.close()


@app.post("/generate-demo-incident")
def generate_demo_incident():

    db: Session = SessionLocal()

    try:

        demo_incidents = [

            {
                "service": "checkout-service",
                "severity": "critical",
                "exception": "ZeroDivisionError",
                "endpoint": "/checkout",
                "stack_trace": "division by zero"
            },

            {
                "service": "db-service",
                "severity": "critical",
                "exception": "ConnectionError",
                "endpoint": "/orders",
                "stack_trace": "database connection timeout"
            },

            {
                "service": "analytics-service",
                "severity": "critical",
                "exception": "MemoryError",
                "endpoint": "/analytics",
                "stack_trace": "memory usage exceeded"
            }
        ]

        data = random.choice(demo_incidents)

        analysis = investigate_incident(
            data["exception"],
            data["stack_trace"]
        )

        current_time = datetime.now().strftime("%H:%M:%S")

        timeline_events.append(
            {
                "time": current_time,
                "event": f"Demo Alert Triggered - {data['service']}"
            }
        )

        timeline_events.append(
            {
                "time": current_time,
                "event": "AI Investigation Started"
            }
        )

        timeline_events.append(
            {
                "time": current_time,
                "event": "Root Cause Identified"
            }
        )

        timeline_events.append(
            {
                "time": current_time,
                "event": "Recovery Plan Generated"
            }
        )

        incident = Incident(
            service=data["service"],
            severity=data["severity"],
            exception=data["exception"],
            endpoint=data["endpoint"],
            stack_trace=data["stack_trace"],
            root_cause=analysis["root_cause"],
            severity_score=analysis["severity_score"],
            fix_suggestion=analysis["fix_suggestion"]
        )

        db.add(incident)
        db.commit()
        db.refresh(incident)

        return {
            "message": "Demo incident created",
            "incident_id": incident.id
        }

    finally:
        db.close()


@app.get("/incidents")
def get_incidents():

    db: Session = SessionLocal()

    try:

        incidents = db.query(Incident).all()

        result = []

        for incident in incidents:

            impact = calculate_business_impact(
                incident.service
            )

            recovery_plan = generate_recovery_plan(
                incident.exception
            )

            code_fix = generate_code_fix(
                incident.exception
                )
            risk = assess_risk(
                incident.exception
                )
            agent_activity = get_agent_activity(
                incident.exception
                )
            reasoning = generate_reasoning(
                incident.exception,
                incident.service
                )
            deployment_steps = []
            if incident.status == "APPROVED":
                deployment_steps = simulate_deployment()
              

            result.append(
                {
                    "id": incident.id,
                    "service": incident.service,
                    "severity": incident.severity,
                    "exception": incident.exception,
                    "endpoint": incident.endpoint,
                    "status": incident.status,
                    "root_cause": incident.root_cause,
                    "fix_suggestion": incident.fix_suggestion,
                    "severity_score": incident.severity_score,
                    "priority": impact["priority"],
                    "customer_impact": impact["customer_impact"],
                    "revenue_risk": impact["revenue_risk"],
                    "users_affected": impact["users_affected"],
                    "escalation_risk": impact["escalation_risk"],
                    "downtime_cost": impact["downtime_cost"],
                    "recovery_plan": recovery_plan,
                    "old_code": code_fix["old_code"],
                    "new_code": code_fix["new_code"],
                    "risk_level": risk["risk_level"],
                    "deployment_recommendation": risk["deployment_recommendation"],
                    "confidence": risk["confidence"],
                    "observation": reasoning["observation"],
                    "analysis": reasoning["analysis"],
                    "hypothesis": reasoning["hypothesis"],
                    "ai_confidence": reasoning["confidence"],
                    "agent_activity": agent_activity,
                    "deployment_steps": deployment_steps
                }
            )

        return result

    finally:
        db.close()


@app.put("/incident/{incident_id}/approve")
def approve_incident(incident_id: int):

    db: Session = SessionLocal()

    try:

        incident = db.query(
            Incident
        ).filter(
            Incident.id == incident_id
        ).first()

        if not incident:
            return {
                "error": "Incident not found"
            }

        if incident.status == "APPROVED":
            return {
                "message": "Incident already approved"
            }

        incident.status = "APPROVED"

        db.commit()

        timeline_events.append(
            {
                "time": datetime.now().strftime("%H:%M:%S"),
                "event": f"Human Approved Fix - Incident #{incident.id}"
            }
        )

        return {
            "message": "Incident approved",
            "incident_id": incident.id
        }

    finally:
        db.close()


@app.get("/agents")
def get_agents():

    return [
        {
            "agent": "Investigator Agent",
            "status": "Completed"
        },
        {
            "agent": "Diagnosis Agent",
            "status": "Completed"
        },
        {
            "agent": "Fix Agent",
            "status": "Completed"
        },
        {
            "agent": "Approval Agent",
            "status": "Awaiting Human Approval"
        }
    ]


@app.get("/timeline")
def get_timeline():

    return timeline_events

@app.get("/metrics")
def get_metrics():

    db: Session = SessionLocal()

    try:

        total_incidents = db.query(
            Incident
        ).count()

        return calculate_metrics(
            total_incidents
        )

    finally:
        db.close()