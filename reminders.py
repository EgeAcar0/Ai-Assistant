from datetime import datetime
from number import text_to_number
from main import get_voice_command
import json
import os

# Kullanıcıdan geçerli bir sayı alana kadar tekrar soran fonksiyon
def get_valid_number(prompt):
    while True:
        response = get_voice_command(prompt)
        number = text_to_number(response)
        if isinstance(number, int):  # Sayıya çevirme başarılıysa döndür
            return number
        print("❌ Geçersiz giriş. Lütfen tekrar söyle.")

# Hatırlatıcı ekleme fonksiyonu
def add_reminder():
    current_year = datetime.now().year

    # Doğrulama ile kullanıcıdan değerleri al
    month = get_valid_number("📅 Lütfen ayı söyleyin (Örnek: 10):")
    day = get_valid_number("📅 Lütfen günü söyleyin (Örnek: 15):")
    hour = get_valid_number("⏰ Lütfen saati söyleyin (Örnek: 14):")
    minute = get_valid_number("⏰ Lütfen dakikayı söyleyin (Örnek: 30):")

    # Hatırlatıcı metni
    task = None
    while not task:  # Boş girişleri önlemek için
        task = get_voice_command("📝 Lütfen hatırlatıcınızı söyleyin:")
        if not task.strip():  # Boşluk karakteri kontrolü
            print("❌ Anlayamadım. Lütfen tekrar söyle.")
            task = None  # Tekrar sormasını sağlamak için None yap

    added_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Hatırlatıcıyı JSON dosyasına ekle
    reminder = {
        "date": f"{current_year}-{month:02d}-{day:02d}",
        "time": f"{hour:02d}:{minute:02d}",
        "task": task,
        "added_date": added_date
    }
    file_path = "reminders.json"

    # Eğer dosya yoksa oluştur
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump([reminder], file, indent=4, ensure_ascii=False)
    else:
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                reminders = json.load(file)
            except json.JSONDecodeError:  # Dosya bozuksa veya boşsa
                reminders = []
        reminders.append(reminder)

        # Türkçe karakterleri destekleyecek şekilde dosyaya yaz
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(reminders, file, indent=4, ensure_ascii=False)

    print("✅ Hatırlatıcı başarıyla eklendi!")



def list_reminders():
    try:
        with open("reminders.json", "r") as file:
            reminders = json.load(file)
            if reminders:
                print("📅 Hatırlatıcılarınız:")
                for index, reminder in enumerate(reminders, start=1):
                    print(f"{index}. Tarih: {reminder['date']}, Saat: {reminder['time']}, Görev: {reminder['task']}")
            else:
                print("📅 Henüz hiç hatırlatıcınız yok.")
    except FileNotFoundError:
        print("❌ Hatırlatıcı dosyası bulunamadı.")












# Hatırlatıcı ekleme fonksiyonu
"""def add_reminder(date, task):
    # Tarih ve saat bilgisini al
    print("📅 Hatırlatıcı hangi tarihe kurulsun? (Örnek: 2023-10-15)")
    date = input("Tarih (YYYY-AA-GG): ")
    print("⏰ Saat kaçta hatırlatılsın? (Örnek: 14:30)")
    time = input("Saat (SS:DD): ")

        # Hatırlatıcı metnini al
    print("📝 Hatırlatıcınız nedir?")
    task = input("Hatırlatıcı: ")

        # Ekleme tarihini al
    added_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Hatırlatıcıyı JSON dosyasına ekle
    reminder = {
        "date": date,
        "time": time,
        "task": task,
        "added_date": added_date
    }

    with open("reminders.json", "r+") as file:
        reminders = json.load(file)
        reminders.append(reminder)
        file.seek(0)
        json.dump(reminders, file, indent=4)

    print("✅ Hatırlatıcı başarıyla eklendi!")"
    """
