import requests

# Hava durumu fonksiyonu
def get_weather(city="aydın"):
    API_KEY = "0a6d1788ebffa57e1bf0eb71b6ea10fd"  # OpenWeatherMap
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=tr&units=metric"
    response = requests.get(url)
    return response.json()


