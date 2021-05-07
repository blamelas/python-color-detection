import cv2
import numpy as np
import os
from matplotlib import pyplot as plot


########################################
# Ler imagem original
img_path = "Resources/Semaforo_verd_2.jpg"
img = cv2.imread(img_path)


########################################
# Mostrar imagem original

cv2.imshow("Imagem Original", img)

cv2.waitKey()



# ##########################
# # Criar e mostrar histogram com libraria matplotlib
#
# plot.hist(img.ravel(), 256, [0, 256])
# plot.show()


##########################
# Criar e mostrar histogram com libraria nativa open cv

hist = cv2.calcHist([img],[0],None,256,[0,255])
cv2.show(hist)



cv2.waitKey()
cv2.destroyAllWindows()






