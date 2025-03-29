import requests
from apis import api_key

# Hava durumu fonksiyonu
def get_weather():
    """
    OpenWeatherMap API'sinden anlık hava durumu verisini çeker.
    API key .env dosyasında 'WEATHER_API_KEY' olarak saklanmalıdır.
    """
    city = "aydın"  # Varsayılan şehir (isteğe bağlı değiştirilebilir)
    
    try:
        response = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=tr"
        )
        response.raise_for_status()  # HTTP hatalarını yakalar
        return response.json()
    except Exception as e:
        print(f"❌ Hava durumu alınamadı: {e}")
        return None