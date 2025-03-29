# Yeni (Google Speech-to-Text)
import speech_recognition as sr
import pyaudio
import json

recognizer = sr.Recognizer()
mic = sr.Microphone()


def get_voice_command(prompt):
    print(prompt)
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="tr-TR")
        print("Algılanan metin:", command)
        return command
    except sr.UnknownValueError:
        print("🤔 Anlayamadım. Lütfen tekrar söyle.")
        return get_voice_command(prompt)
    except sr.RequestError:
        print("❌ API isteği başarısız oldu.")
        return None

print("Dinliyorum... (Çıkmak için CTRL+C)")