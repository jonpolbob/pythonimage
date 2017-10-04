#exemples d'utilisation de scikit image pour le traitement d'image

import numpy as np
import skimage
from skimage import data
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib as mp


dataimage = data.imread("c:\\tmp\\img-bee2.jpg")
#io.imread() marche aussi

print (type(dataimage))
print (dataimage.shape)  #on a un trilopet sisex, sizey, nbplans

#grayimg=dataimage[:,:,1]  conersion bourrin en gris
grayimg = skimage.color.rgb2gray(dataimage)  #conversion en gris avec skimage

plt.imshow(grayimg, cmap='gray')
plt.show()

print('ok')




