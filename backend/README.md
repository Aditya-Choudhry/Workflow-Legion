# Backend

## Local run

`powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload`

Health check:

http://localhost:8000/health
