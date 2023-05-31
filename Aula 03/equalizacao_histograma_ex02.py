from matplotlib import pyplot as plt
import numpy as np
import cv2
import imageio

img = cv2.imread('images/ponte.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converte P&B

h_eq = cv2.equalizeHist(img)

plt.figure()
plt.title("Histograma Equalizado")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(h_eq.ravel(), 256, [0,256])
plt.xlim([0, 256])
plt.show()

plt.figure()
plt.title("Histograma Original")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(img.ravel(), 256, [0,256])
plt.xlim([0, 256])
plt.show()


cv2.imwrite('./images/ponte_result.jpg',h_eq)

result = imageio.imread("./images/ponte_result.jpg")

fig, axes = plt.subplots(1, 2, figsize=(10, 6))
ax = axes.ravel()

ax[0].imshow(img, cmap=plt.cm.gray)
ax[0].set_title("Imagem Original")

ax[1].imshow(result, cmap=plt.cm.gray)
ax[1].set_title("Imagem melhorada - Histograma Equalizado")

fig.tight_layout()



cv2.waitKey(0)