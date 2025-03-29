from reminders import add_reminder, list_reminders
from weather import get_weather
from main import get_voice_command, mic
from send_command import send_command
import os



try:
    while True:
        # Sesli komut al
        command = get_voice_command("")
        if command:
            # Aktivasyon kelimesi algılandığında
            if "merhaba" in command.lower():
                print("✅ Aktivasyon kelimesi algılandı!")
                command = get_voice_command("🛠️ Komut bekleniyor...")

                # Komut dinle
                while True:
                    if command:
                        # Komutları işle
                        if "opera" in command:
                            print("🖥️ Opera açılıyor...")
                            os.startfile("C:/Users/EgePc/AppData/Local/Programs/Opera GX/opera.exe")  # Windows
                            break
                        elif "youtube" in command:
                            print("📱 YouTube açılıyor...")
                            send_command("phone", "open_youtube")
                            break
                        elif "hava durumu" in command:
                            weather = get_weather()
                            print(f"🌤️ Hava durumu: {weather['weather'][0]['description']}, Sıcaklık: {weather['main']['temp']}°C")
                            break
                        elif "hatırlatıcı ekle" in command:
                            add_reminder()
                        elif "hatırlatıcılarım neler" in command:
                            list_reminders()
                            break
                        else:
                            print("🤔 Anlayamadım. Lütfen tekrar söyle.")
                            break
except KeyboardInterrupt:


    print("Kapatılıyor...")