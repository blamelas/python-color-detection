import cv2
import numpy as np
import os
from matplotlib import pyplot as plot

nimagensCropadas=0

######################################################
# Ler Imagem V1
imgV1 = cv2.imread("Resources/Semaforo_verd_1.jpg")

# Calcular Tamanho
print(imgV1.shape)
cv2.imshow("Imagem Original",imgV1)

cv2.waitKey()

# Cropar
imgCroppedV1 = imgV1[41:131,52:88]

# Mostrar Crop com valores verifricados na janel de visualização
cv2.imshow("Imagem Cropada",imgCroppedV1)

nImagensCropadas = nimagensCropadas + 1

print("Imagem Cortada")
cv2.waitKey()

# Gravar Crop nova imagem em pasta crop
cv2.imwrite("Resources/Crop_images/Semaforo_verd_1_Crop.jpg", imgCroppedV1)


######################################################
# Ler Imagem V2
imgV2 = cv2.imread("Resources/Semaforo_verd_2.jpg")

# Calcular Tamanho
print(imgV2.shape)
cv2.imshow("Imagem Original V2",imgV2)

cv2.waitKey()

# Cropar Primeiro parametro primeiro eixo Y e depois X
imgCroppedV2 = imgV2[26:145,54:104]
imgCroppedV2b = imgV2[25:147,190:241]


# Mostrar Crop com valores verifricados na janel de visualização
cv2.imshow("Imagem Cropada",imgCroppedV2)
cv2.imshow("Imagem Cropada",imgCroppedV2b)

nImagensCropadas = nimagensCropadas + 1

print("Imagem Cortada")
cv2.waitKey()

# Gravar Crop nova imagem em pasta crop
cv2.imwrite("Resources/Crop_images/Semaforo_verd_2_Crop.jpg", imgCroppedV2)
cv2.imwrite("Resources/Crop_images/Semaforo_verd_2b_Crop.jpg", imgCroppedV2b)


######################################################
# Ler Imagem V3
imgV3 = cv2.imread("Resources/Semaforo_verd_3.jpg")

# Calcular Tamanho
print(imgV3.shape)
cv2.imshow("Imagem Original V3",imgV3)

cv2.waitKey()

# Cropar Primeiro parametro primeiro eixo Y e depois X
imgCroppedV3 = imgV3[37:158,60:100]

# Mostrar Crop com valores verifricados na janel de visualização
cv2.imshow("Imagem Cropada",imgCroppedV3)

nImagensCropadas = nimagensCropadas + 1

print("Imagem Cortada")
cv2.waitKey()

# Gravar Crop nova imagem em pasta crop
cv2.imwrite("Resources/Crop_images/Semaforo_verd_3_Crop.jpg", imgCroppedV3)



######################################################
# Ler Imagem V4
imgV4 = cv2.imread("Resources/Semaforo_verd_4.jpg")

# Calcular Tamanho
print(imgV4.shape)
cv2.imshow("Imagem Original",imgV4)

cv2.waitKey()

# Cropar Primeiro parametro primeiro eixo Y e depois X
imgCroppedV4 = imgV4[24:73,189:210]

# Mostrar Crop com valores verifricados na janel de visualização
cv2.imshow("Imagem Cropada",imgCroppedV4)

nImagensCropadas = nimagensCropadas + 1

cv2.waitKey()

cv2.imshow("imagem cropada v2", imgCroppedV2b)

cv2.waitKey()

# Gravar Crop nova imagem em pasta crop
cv2.imwrite("Resources/Crop_images/Semaforo_verd_4_Crop.jpg", imgCroppedV4)