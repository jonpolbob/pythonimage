#exemples d'utilisation de scikit image pour le traitement d'image

import numpy as np
import skimage
from skimage import data
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib as mp



dataimage = data.imread("c:\\tmp\\microplate.jpg")
#io.imread() marche aussi

print (type(dataimage))
print (dataimage.shape)  #on a un trilopet sisex, sizey, nbplans

#grayimg=dataimage[:,:,1]  conersion bourrin en gris
grayimg = skimage.color.rgb2gray(dataimage)  #conversion en gris avec skimage

plt.imshow(grayimg, cmap='gray')
plt.show()

#extraction de sous image
subimage = grayimg[23:24,100:200]

subimage2 = grayimg[23:24,150:250]

print (subimage.shape)
print (subimage2.shape)

resu=[]
for decl in range(1,100):
    subimage2 = grayimg[23:24,150+decl:250+decl]
    resu.append(np.correlate(subimage[:,0],subimage2[:,0]))

plt.plot(resu)
plt.show()



