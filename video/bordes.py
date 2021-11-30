import cv2
import numpy as np

captura = cv2.VideoCapture(0)

while True:
    ret, frame = captura.read()
    image = frame
    if not ret:
        break

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.GaussianBlur(frame, (3, 3), 0)
    frame = cv2.Canny(frame, 50, 150)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    frame = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel, iterations=2)

    cnts = cv2.findContours(frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    total = 0
    for c in cnts:
        area = cv2.contourArea(c)
        #print(area)

        if area > 2000:
            total += 1
            cv2.drawContours(image, [c], -1, (0, 0, 255), 3)

    texto = "Bordes: {}".format(total)
    cv2.putText(image, texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('image', image)


    tecla = cv2.waitKey(1) & 0xFF
    if tecla == ord('q'):
        break