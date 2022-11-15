from vosk import Model, KaldiRecognizer  # оффлайн-распознавание от Vosk
import speech_recognition  # распознавание пользовательской речи (Speech-To-Text)
import wave  # создание и чтение аудиофайлов формата wav
import json  # работа с json-файлами и json-строками
import os  # работа с файловой системой
from pioneer_sdk import Pioneer, Camera
import cv2
import numpy as np

pioneer_mini = Pioneer()
camera = Camera()

def record_and_recognize_audio(*args: tuple):
    """
    Online Part
    """
    with microphone:
        recognized_data = ""

        recognizer.adjust_for_ambient_noise(microphone, duration=2)

        try:
            print("Listening...")
            audio = recognizer.listen(microphone, 5, 5)

            with open("microphone-results.wav", "wb") as file:
                file.write(audio.get_wav_data())

        except speech_recognition.WaitTimeoutError:
            print("Can you check if your microphone is on, please?")
            return

        try:
            print("Started recognition...")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass

        except speech_recognition.RequestError:
            print("Trying to use offline recognition...")
            recognized_data = use_offline_recognition()

        return recognized_data


def use_offline_recognition():
    """
    Offline Part
    """
    recognized_data = ""
    try:
        wave_audio_file = wave.open("microphone-results.wav", "rb")
        model = Model("models/vosk-model-small-ru-0.4")
        offline_recognizer = KaldiRecognizer(model, wave_audio_file.getframerate())

        data = wave_audio_file.readframes(wave_audio_file.getnframes())
        if len(data) > 0:
            if offline_recognizer.AcceptWaveform(data):
                recognized_data = offline_recognizer.Result()

                recognized_data = json.loads(recognized_data)
                recognized_data = recognized_data["text"]
                if recognized_data == "взлетай":
                    pioneer_mini.arm()
                    pioneer_mini.takeoff()
                if recognized_data == "садись":
                    pioneer_mini.land()
                    pioneer_mini.disarm()

    except:
        print("Sorry, speech service is unavailable. Try again later")

    return recognized_data


if __name__ == "__main__":

    # инициализация инструментов распознавания и ввода речи
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    while True:
        """
        Record Part
            """
        voice_input = record_and_recognize_audio()
        os.remove("microphone-results.wav")
        print(voice_input)