import cv2

# Захват видео с камеры ноутбука
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Получаем изображение
    cv2.imshow('video', frame)  # Выводим изображение на экран

    if cv2.waitKey(1) & 0xFF == 27:  # Выход из программы, если нажали ESC
        break

cap.release()  # Отпускаем захват камеры
cv2.destroyAllWindows()  # Закрываем все открытые окна
