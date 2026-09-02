# Async DevOps Lab

This project demonstrates how to use Python's `async/await` to build efficient monitoring and automation workflows.  
It includes a FastAPI service with `/ping` and `/health` endpoints, plus scripts that poll multiple endpoints concurrently.  
The goal is to show how asynchronous programming can reduce wait times and scale monitoring across many systems.

## Features
- **[FastAPI service](ca://s?q=Build_FastAPI_service_with_async)** with `/ping` and `/health` endpoints.
- **[Async basics](ca://s?q=Python_async_basics)**: simple coroutines with `async def` and `await`.
- **[Concurrent tasks](ca://s?q=Run_multiple_async_tasks_in_Python)** using `asyncio.gather`.
- **[Async HTTP requests](ca://s?q=Async_HTTP_requests_in_Python)** with aiohttp.
- **[Monitoring script](ca://s?q=Async_polling_multiple_VM_endpoints)** that polls endpoints concurrently, simulating DevOps health checks.


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
