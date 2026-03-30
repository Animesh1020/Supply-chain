import requests
from config.settings import BASE_URL

def forward_data(payload):
    try:
        response = requests.post(BASE_URL, json=payload)
        return response.status_code, response.json()
    except Exception as e:
        return 500, {"error": str(e)}