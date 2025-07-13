from fastapi import FastAPI
from pydantic import BaseModel
from lead_scoring import score_lead, confidence_level, estimate_revenue, verify_email

app = FastAPI()

class Lead(BaseModel):
    name: str
    email: str
    job_title: str
    company: str
    domain: str
    location: str
    linkedin: str

@app.post("/score")
def score_lead_api(lead: Lead):
    row = lead.dict()
    score = score_lead(row)
    return {
        "lead_score": score,
        "confidence_level": confidence_level(score),
        "estimated_revenue": estimate_revenue(row),
        "email_validity": verify_email(row["email"])
    }
