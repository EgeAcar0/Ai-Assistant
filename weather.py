import requests
from apis import api_key

# Hava durumu fonksiyonu
def get_weather(city="aydın"):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=tr&units=metric"
    response = requests.get(url)
    return response.json()


