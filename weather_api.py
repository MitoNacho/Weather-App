import requests
from config import API_KEY

city = "Oviedo"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

print(response.json())