import speech_recognition
from pioneer_sdk import Pioneer, Camera
import numpy as np
import cv2

pioneer_mini = Pioneer()
camera = Camera()

if __name__ == "__main__":

    # инициализация инструментов распознавания и ввода речи
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()


    def record_and_recognize_audio(*args: tuple):
        count = 0
        """
        Запись и распознавание аудио
        """
        with microphone:
            recognized_data = ""
            if recognized_data == "взлетай":
                count = 1
            # регулирование уровня окружающего шума
            # recognizer.adjust_for_ambient_noise(microphone, duration=2)

            try:
                print("Listening...")
                audio = recognizer.listen(microphone, 5, 5)

            except speech_recognition.WaitTimeoutError:
                print("Can you check if your microphone is on, please?")
                return

            # использование online-распознавания через Google
            try:
                print("Started recognition...")
                recognized_data = recognizer.recognize_google(audio, language="ru").lower()
                # if recognized_data == "взлетай":
                  #  pioneer_mini.arm()
                   # pioneer_mini.takeoff()
                #if recognized_data == "садись":
                 #   pioneer_mini.land()
                  #  pioneer_mini.disarm()
            except speech_recognition.UnknownValueError:
                pass

            # в случае проблем с доступом в Интернет происходит выброс ошибки
            except speech_recognition.RequestError:
                print("Check your Internet Connection, please")

            return recognized_data


    while True:
        # старт записи речи с последующим выводом распознанной речи
        voice_input = record_and_recognize_audio()
        print(voice_input)
