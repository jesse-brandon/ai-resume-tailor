import json

import requests

URL = "http://localhost:8000/data/import-resume"

with open("examples/sample_resume.json") as f:
    payload = json.load(f)

response = requests.post(URL, json=payload)

print("Status Code:", response.status_code)

try:
    print("Response:", response.json())
except Exception:
    print("Raw Response:", response.text)
