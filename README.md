# Locust Performance Testing – ReqRes API

## Project Overview
This project demonstrates performance and load testing using Locust
on the ReqRes public REST API.

## Tools & Technologies
- Python
- Locust
- REST APIs

## APIs Tested
- GET /api/users?page=2
- GET /api/users/2
- POST /api/users

## Test Scenarios
- Simulated concurrent users
- Read-heavy traffic with write operations
- Weighted task execution
- Response status validation

## How to Run
1. Install dependencies:
   pip install -r requirements.txt
2. Run Locust:
   locust
3. Open browser:
   http://localhost:8089
4. Start test with configured users and spawn rate

## Notes
ReqRes is a public API. Tests were executed with limited load to avoid abuse.

## Author
QA Engineer with 3+ years of experience in Automation, API, and Performance Testing
