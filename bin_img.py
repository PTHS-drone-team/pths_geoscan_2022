import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 800)
cap.set(4, 600)

while True:
    success, img = cap.read()
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # перевод ч/б картинку

    img = cv2.Canny(img, 150, 150) # создание бинарного изображения

    kernel = np.ones((4,4), np.uint8) # создание матрицы состоящей из единиц
    img = cv2.dilate(img, kernel, iterations=1) # расширяем точки
    img = cv2.erode(img, kernel, iterations=1) # эрозия
    cv2.imshow('test', img)

    key = cv2.waitKey(1)
    if key & 0xFF == 27:
        break