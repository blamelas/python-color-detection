import cv2
import numpy as np
import os
from matplotlib import pyplot as plot


########################################
# Ler imagem original
img_path = "Resources/Semaforo_verm_5.jpg"
img = cv2.imread(img_path)

redPixels=0
yellowPixels=0
greenPixels=0
numero_redlights=0
numero_greenlights=0
numero_yellowlights=0


# Aplicar Blur
img_blur = cv2.medianBlur(img,5)

# Converter para HSV
img_hsv = cv2.cvtColor(img_blur, cv2.COLOR_BGR2HSV)

# Criar Array com o numpy para consultar dados recebidos doa HSV
img_HSV_values = np.array(img_hsv)

# # Mostrar dados array valores HSV
# print(img_HSV_values)




# Mostrar imagem original
cv2.imshow('Original', img)

cv2.waitKey()



########################################
# Red Color Range de HSV
lower_range_red = np.array([161, 155, 84])
upper_range_red = np.array([179, 255, 255])

# Criar mascara à volta da zona RED
red_mask = cv2.inRange(img_hsv, lower_range_red, upper_range_red)

# Função para apenas a zona vermelha
red_only = cv2.bitwise_and(img_hsv, img, mask=red_mask)

# Mostrar mascaras aplicadas à zona red
cv2.imshow("mascara red", red_mask)
#cv2.imshow("mascara red", red_only)
redPixels = cv2.countNonZero(red_mask)

print("Pixels Vermelhos " + str(redPixels))
cv2.waitKey()



########################################
# Green Color Range de HSV
lower_range_green = np.array([48, 208, 0])
upper_range_green = np.array([83, 255, 255])

# Criar máscara à volta da zona Green
green_mask = cv2.inRange(img_hsv, lower_range_green, upper_range_green)

# Mostrar apenas a zona Green
green_only = cv2.bitwise_and(img_hsv, img, mask=green_mask)

# Mostrar mascaras aplicadas à zona red
cv2.imshow("mascara Green", green_mask)
#cv2.imshow("mascara Green", green_only)
greenPixels = cv2.countNonZero(green_mask)

print("Pixels Verdes " + str(greenPixels))
cv2.waitKey()



########################################
# Yellow Color Range de HSV
lower_range_yellow = np.array([12, 173, 155])
upper_range_yellow = np.array([42, 212, 255])

# Criar máscara à volta da zona yellow
yellow_mask = cv2.inRange(img_hsv, lower_range_yellow, upper_range_yellow)

# Mostrar apenas a zona Green
yellow_only = cv2.bitwise_and(img_hsv, img, mask=yellow_mask)

# Mostrar mascaras aplicadas à zona red
cv2.imshow("mascara Yellow", yellow_mask)
#cv2.imshow("mascara Yellow", yellow_only)
yellowPixels = cv2.countNonZero(yellow_mask)

print("Pixels Amarelos " + str(yellowPixels))
cv2.waitKey()


if redPixels > 0:
    numero_redlights = numero_redlights + 1
    print ("Está Amarelo em "+str(numero_redlights)+" Imagens")

if greenPixels > 0:
    numero_redlights = numero_redlights + 1
    print ("Está Verde em "+str(numero_greenlights)+" Imagens")

if yellowPixels > 0:
    print ("Está Amarelo em "+str(numero_yellowlights)+" Imagens")

cv2.waitKey()



