
import requests

city = "Bengaluru"
url = "https://wttr.in/" + city + "?format=j1"

response = requests.get(url, timeout=10)

if response.ok:
    data = response.json()
    current = data["current_condition"][0]
    print("City:", city)
    print("Temperature:", current["temp_C"], "C")
    print("Humidity:", current["humidity"], "%")
    print("Weather:", current["weatherDesc"][0]["value"])
else:
    print("Weather service unavailable")
