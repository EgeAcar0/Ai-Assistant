import requests
from apis import api_url


# API'ye komut gönderme fonksiyonu
def send_command(device, command):
    try:
        response = requests.post(api_url, json={"device": device, "command": command})
        response.raise_for_status()  # HTTP hatalarını yakala
        print("API Yanıtı:", response.json())
    except requests.exceptions.RequestException as e:
        print("API isteği başarısız oldu:", e)

        