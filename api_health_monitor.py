import requests
from datetime import datetime

endpoints = {
    "Authentication": "https://example.com/auth",
    "Payments": "https://example.com/payments",
    "Users": "https://example.com/users"
}
for service, url in endpoints.items():
    try:
        response = requests.get(url, timeout=5)
        print(datetime.now(), service, response.status_code)
    except requests.RequestException:
        print(datetime.now(), service, "SERVICE UNAVAILABLE")
