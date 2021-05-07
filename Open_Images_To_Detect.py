import cv2
import numpy as np
import os
from matplotlib import pyplot as plot


########################################
# Caminho das imagens
path_of_images = r"/Users/brunolamelas/PycharmProjects/ColorDetection_MiniProject_01/resources/"
list_of_images = os.listdir(path_of_images)

# Variaveis para contar pixels de cada gama e contador para numero de vezes que cada semáforo é visto

redPixels=0
yellowPixels=0
greenPixels=0
numero_redlights=0
numero_greenlights=0
numero_yellowlights=0
n_imagem_lidas = 0


########################################
# Ciclo For para ler cada uma por ordem
for image in list_of_images:
    img = cv2.imread(os.path.join(path_of_images, image))

    n_imagem_lidas = n_imagem_lidas + 1

    print("///////////////////////////////// Imagem Lida Número " + str(n_imagem_lidas))

    # Converter para HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    print("imagem convertida para HSV")

    cv2.waitKey()


    ########################################
    # Red Color Range de HSV
    lower_range_red = np.array([161, 155, 84])
    upper_range_red = np.array([179, 255, 255])

    # Criar mascara à volta da zona RED
    red_mask = cv2.inRange(img_hsv, lower_range_red, upper_range_red)
    cv2.imshow("mascara red", red_mask)
    redPixels = cv2.countNonZero(red_mask)
    print("Pixels Vermelhos " + str(redPixels))
    print("Máscara Red Pixels Criada")

    cv2.waitKey()




    ########################################
    # Green Color Range de HSV
    lower_range_green = np.array([57, 134, 142])
    upper_range_green = np.array([96, 201, 255])


    # Criar máscara à volta da zona Green
    green_mask = cv2.inRange(img_hsv, lower_range_green, upper_range_green)
    cv2.imshow("mascara Green", green_mask)
    greenPixels = cv2.countNonZero(green_mask)
    print("Pixels Verdes " + str(greenPixels))
    print("Máscara Green Pixels Criada")

    cv2.waitKey()



    ########################################
    # Yellow Color Range de HSV

    lower_range_yellow = np.array([10, 115, 173])
    upper_range_yellow = np.array([24, 225, 255])

    # lower_range_yellow = np.array([14, 131, 152])
    # upper_range_yellow = np.array([32, 255, 255])

    # Criar máscara à volta da zona yellow
    yellow_mask = cv2.inRange(img_hsv, lower_range_yellow, upper_range_yellow)
    cv2.imshow("mascara yellow", yellow_mask)
    yellowPixels = cv2.countNonZero(yellow_mask)
    print("Pixels Amarelos " + str(yellowPixels))
    print("Máscara Yellow Pixels Criada")

    cv2.waitKey()

    cv2.imshow("Imagem", img)

    ########################################
    # Fim de Ciclo For para ler cada uma por ordem
    print("///////////////////////////////// Estado Semáforo")
    if redPixels > 0:
        numero_redlights = numero_redlights + 1
        print("Está Vermelho")
    else:
        print("Não está Vermelho")

    if greenPixels > 0:
        numero_greenlights = numero_greenlights + 1
        print("Está Verde")
    else:
        print("Não está Verde")

    if yellowPixels > 0:
        numero_yellowlights = numero_yellowlights + 1
        print("Está Amarelo")
    else:
        print("Não está Amarelo")


    ########################################
    # Zerar Variáveis que contam presença de pixels das gamas(RED/GREEN/Yellow)

    redPixels = 0
    yellowPixels = 0
    greenPixels = 0


    ########################################
    # Apresentar Totais

    cv2.waitKey()
    print("///////////////////////////////// TOTAIS")
    print("Total de Imagens com semáforo Vermelho: " + str(numero_redlights))
    print("Total de Imagens com semáforo Verde: " + str(numero_greenlights))
    print("Total de Imagens com semáforo Amarelo: " + str(numero_yellowlights))


    cv2.destroyAllWindows()
