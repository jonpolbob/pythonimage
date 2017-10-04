#exemples d'utilisation de scikit image pour le traitement d'image
#recherche intercorrelation de one clickee
import numpy as np
import skimage
from skimage import data
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib as mp

numclick=0
ix1=0
ix2=0
iy1=0
iy2=0
resu = None
changed =0

def onclick(event):
    global numclick
    global ix1,ix2,iy1,iy2

    if numclick ==0:
        ix1 = event.xdata
        iy1 = event.ydata
    if numclick == 1:
        ix2 = event.xdata
        iy2 = event.ydata
    numclick = 1-numclick
    if numclick==0:
        processcorrelation()


def processcorrelation():
    global resu
    global grayimg
    global ax2
    global ix1, ix2, iy1, iy2
    global changed

    changed =1
    resu =[]
    #norm = np.linalg.norm(grayimg[iy1:iy1+1, ix1:ix2],ord=1)
    #subimage = grayimg[iy1:iy1+1, ix1:ix2]/norm
    submatrix = grayimg[iy1:iy1+1, ix1:ix2]
    i = submatrix.min()
    j=submatrix.ptp()
    subimage = (submatrix-submatrix.min())/submatrix.ptp() #valeur-min/peak to peak
    for decl in range(0,130):
        step = 5*decl
        submatrix2 = grayimg[iy1:iy1+1,ix1+step:ix2+step]
        subimage2 = (submatrix2-submatrix2.min())/submatrix2.ptp()
        #norm2 = np.linalg.norm(grayimg[iy1:iy1+1,ix1+step:ix2+step],ord=1)
        #subimage2 = grayimg[iy1:iy1+1,ix1+step:ix2+step]/norm2
        resu.append(np.correlate(subimage[:,0],subimage2[:,0])[0])

    print(resu)
    #plt.show()


#le main
dataimage = data.imread("c:\\tmp\\microplate.jpg")
#io.imread() marche aussi

print (type(dataimage))
print (dataimage.shape)  #on a un trilopet sisex, sizey, nbplans

#grayimg=dataimage[:,:,1]  conersion bourrin en gris
grayimg = skimage.color.rgb2gray(dataimage)  #conversion en gris avec skimage

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(211) #2 dessins
ax2 = fig.add_subplot(212)  # 2 dessins

fig.canvas.mpl_connect('button_press_event',onclick)

ax.imshow(grayimg, cmap='gray')
plt.draw()

#boucle pour mettre a jour en laissant le ion tourner
while True:
    plt.pause(.05)
    if changed ==1:
        ax2.clear()
        ax2.plot(range(0,650,5),resu)
        plt.draw()
        changed=0#plt.draw()

print("fin")

