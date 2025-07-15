import requests
import hashlib
import json

API_ID = "3124071772711358"
API_SECRET = "44e591328af7f5403301f01e6f8ba80f"
EMAIL = "vitaliy.sharaevskiy@gmail.com"
PASSWORD = "2025Vaschenko7"

def send_request():
    password_sha256 = hashlib.sha256(PASSWORD.encode("utf-8")).hexdigest()

    try:
        response = requests.post(
            url="https://api.solarmanpv.com/account/v1.0/token",
            params={
                "appId": API_ID,
                "language": "en",
            },
            headers={
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "email": EMAIL,
                "password": password_sha256,
                "appSecret": API_SECRET
            })
        )
        print('Response HTTP Status Code:', response.status_code)
        print('Response HTTP Response Body:', response.text)
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

send_request()
