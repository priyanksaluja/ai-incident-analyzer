# AI Incident Analyzer

An intelligent API service that analyzes system logs and incidents to detect root causes and suggest resolution actions using pattern matching and RAG (Retrieval-Augmented Generation) techniques.

## Overview

The AI Incident Analyzer is a FastAPI-based application that:
- Processes system logs and identifies critical errors
- Matches error patterns against a knowledge base of known incidents
- Detects probable root causes
- Suggests actionable remediation steps

## Features

- 🔍 **Log Analysis**: Processes system logs to identify critical errors and warnings
- 🎯 **Pattern Matching**: Matches log patterns against a database of known incidents
- 🧠 **Root Cause Detection**: Automatically identifies probable root causes using pattern matching
- 💡 **Smart Suggestions**: Provides resolution recommendations for detected issues
- 📊 **Summary Generation**: Creates concise summaries of system health status
- 🚀 **RESTful API**: Easy-to-use HTTP endpoints for integration

## Tech Stack

- **Framework**: FastAPI
- **Server**: Uvicorn
- **Data Validation**: Pydantic
- **Environment Management**: python-dotenv

## Project Structure

```
ai-incident-analyzer/
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
└── app/
    ├── __init__.py
    ├── main.py              # FastAPI application and endpoints
    ├── analyzer.py          # Log analysis and root cause detection logic
    ├── rag.py              # RAG (Retrieval-Augmented Generation) utilities
    ├── models.py           # Pydantic data models
    └── data/
        ├── logs.json       # Sample system logs
        └── incidents.json  # Known incident patterns and resolutions
```

## Installation

### Prerequisites
- Python 3.8 or higher
- Virtual environment (recommended)

### Setup

1. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Dependencies

- `fastapi` - Modern web framework for building APIs
- `uvicorn` - ASGI server for running FastAPI applications
- `pydantic` - Data validation using Python type annotations
- `python-dotenv` - Load environment variables from .env file

## Running the Application

### Development Mode

Run the application with auto-reload enabled:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### Interactive API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### 1. Home Endpoint
```
GET /
```
Returns a welcome message confirming the API is running.

**Response**:
```json
{
  "message": "AI-powered Incident Analysis API"
}
```

### 2. Analyze Endpoint
```
GET /analyze
```
Analyzes system logs and detects root causes of incidents.

**Response**:
```json
{
  "summary": "1 critical errors detected across systems.",
  "probable_root_cause": "Missing or corrupted trade file",
  "suggested_action": "Re-upload file and re-run ingestion job"
}
```

## Data Format

### Logs Format (logs.json)

Each log entry contains:
- `timestamp` (string): ISO 8601 format timestamp
- `system` (string): Name of the system that generated the log
- `level` (string): Log severity level (ERROR, WARN, INFO, etc.)
- `message` (string): Detailed log message

**Example**:
```json
{
  "timestamp": "2026-03-20T02:00:00",
  "system": "TradeIngestion",
  "level": "ERROR",
  "message": "File ingestion failed for trades_20260320.csv"
}
```

### Incidents Format (incidents.json)

Each incident pattern contains:
- `id` (string): Unique incident identifier
- `pattern` (string): Text pattern to match in logs
- `root_cause` (string): Description of the root cause
- `resolution` (string): Suggested resolution steps

**Example**:
```json
{
  "id": "INC001",
  "pattern": "file ingestion failed",
  "root_cause": "Missing or corrupted trade file",
  "resolution": "Re-upload file and re-run ingestion job"
}
```

## How It Works

1. **Log Loading**: The `/analyze` endpoint loads system logs from `logs.json`
2. **Incident Loading**: Known incident patterns are retrieved from `incidents.json`
3. **Log Summary**: Critical errors are counted and summarized
4. **Pattern Matching**: Each log message is matched against known incident patterns
5. **Root Cause Detection**: When a match is found, the associated root cause is returned
6. **Response**: The analysis result is returned with summary, root cause, and suggested action

## Example Workflow

```
Input Logs
    ↓
[Load & Parse Logs]
    ↓
[Count Critical Errors]
    ↓
[Match Patterns Against Incidents]
    ↓
[Get Root Cause & Resolution]
    ↓
Output: AnalysisResponse
```

## Response Model

The API returns analysis results using the `AnalysisResponse` model:

```python
class AnalysisResponse(BaseModel):
    summary: str                    # Summary of log analysis
    probable_root_cause: str        # Detected root cause
    suggested_action: str           # Recommended action
```

## Development Notes

### Adding New Incident Patterns

Update `app/data/incidents.json` with new patterns:

```json
{
  "id": "INC003",
  "pattern": "your pattern here",
  "root_cause": "Description of what causes this issue",
  "resolution": "Steps to resolve this issue"
}
```

### Log Processing

The analyzer looks for error-level logs and attempts to match their messages against known incident patterns. Matches are case-insensitive for pattern matching.

## Future Enhancements

- [ ] Integration with external log management systems (ELK, Splunk)
- [ ] Machine learning-based root cause detection
- [ ] Multi-factor incident correlation
- [ ] Real-time log streaming and analysis
- [ ] Custom incident pattern creation via API
- [ ] Historical trend analysis
- [ ] Alert thresholds and notifications
- [ ] PostgreSQL backend for persistent storage

## Error Handling

If no matching incident pattern is found:
- `probable_root_cause`: "Unknown"
- `suggested_action`: "Manual investigation required"

## License

MIT License


## Contact

For questions or issues, please open an issue in the project repository.