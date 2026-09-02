# Async DevOps Lab

Python scripts and FastAPI service demonstrating async/await for monitoring and automation.


## Installation

1-Clone the repo:


git clone https://github.com/Stevmong/python-async-devops-lab.git
cd python-async-devops-lab


2-Create a virtual environment:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


3-Usage Instructions

Start the FastAPI service:
bash
uvicorn main:app --reload


Test endpoints:

http://127.0.0.1:8000/ping → returns {"message":"pong"}

http://127.0.0.1:8000/health → returns uptime and status

Run monitoring script:

bash
python3 health_check.py
DevOps Context

markdown
4- DevOps Context

- `/ping` simulates a liveness probe (is the service alive?).
- `/health` simulates a readiness probe (is the service healthy?).
- `health_check.py` polls endpoints concurrently using async/await, similar to how monitoring tools check multiple VMs at once.
Dependencies

markdown

5- Dependencies

- Python 3.10+
- FastAPI
- Uvicorn
- aiohttp
