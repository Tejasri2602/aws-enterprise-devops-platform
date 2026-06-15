
import requests

URL = "http://localhost:5000/health"

try:
    response = requests.get(URL, timeout=5)

    if response.status_code == 200:
        print("Application Healthy")
    else:
        print("Application Unhealthy")

except Exception as e:
    print(f"Error: {e}")
