import cv2
import numpy as np

####codigo para ler a captura da webcam
cap = cv2.VideoCapture(1)
while True:

    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)



    #Red Color



    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break


cv2.waitKey()
cv2.destroyAllWindows()