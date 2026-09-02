# Async DevOps Lab

Python scripts and FastAPI service demonstrating async/await for monitoring and automation.

## How to Test

1. Clone the repo:
   ```bash
   git clone https://github.com/Stevmong/python-async-devops-lab.git
   cd python-async-devops-lab


2-Create a virtual environment, Install dependencies with pip install -r requirements.txt.

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


3-Run FastAPI:

uvicorn main:app --reload



Test endpoints:

http://127.0.0.1:8000/ping → returns {"message":"pong"}

http://127.0.0.1:8000/health → returns uptime and status

Run monitoring script:

bash
python3 health_check.py
