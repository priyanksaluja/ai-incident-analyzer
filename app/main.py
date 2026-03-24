from fastapi import FastAPI
from app.analyzer import load_logs, summarize_logs, detect_root_cause
from app.rag import load_incidents
from app.models import AnalysisResponse

app = FastAPI(title="AI Incident Analyzer")

@app.get("/")
def home():
    return {"message": "AI-powered Incident Analysis API"}

@app.get("/analyze", response_model=AnalysisResponse)
def analyze():
    logs = load_logs()
    incidents = load_incidents()

    summary = summarize_logs(logs)
    incident = detect_root_cause(logs, incidents)

    if incident:
        return AnalysisResponse(
            summary=summary,
            probable_root_cause=incident["root_cause"],
            suggested_action=incident["resolution"]
        )

    return AnalysisResponse(
        summary=summary,
        probable_root_cause="Unknown",
        suggested_action="Manual investigation required"
    )
