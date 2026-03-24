import json

def load_logs():
    with open("app/data/logs.json") as f:
        return json.load(f)

def summarize_logs(logs):
    errors = [log for log in logs if log["level"] == "ERROR"]
    return f"{len(errors)} critical errors detected across systems."

def detect_root_cause(logs, incidents):
    for log in logs:
        for incident in incidents:
            if incident["pattern"] in log["message"].lower():
                return incident
    return None
