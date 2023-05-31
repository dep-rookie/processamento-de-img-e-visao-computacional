import cv2
import numpy
import matplotlib.pyplot as plt
import imageio
from skimage import data
from skimage.color import rgb2gray
 
# Carregando a imagem
img = cv2.imread('./images/resized-pout.jpg')
img_to_yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)

# Equalizando o histograma
img_to_yuv[:,:,0] = cv2.equalizeHist(img_to_yuv[:,:,0])
hist_equalization_result = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)
 
# Salvando o histograma equalizado
cv2.imwrite('./images/resized-pout_result.jpg',hist_equalization_result)

# Lendo o histograma equalizado salvo.
result = imageio.imread("./images/resized-pout_result.jpg")

# Histograma da imagem 
plt.hist(img.ravel(),256,[0,256])
plt.hist(result.ravel(),256,[0,256])

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax = axes.ravel()

ax[0].imshow(img)
ax[0].set_title("Imagem Original")

ax[1].imshow(result, cmap=plt.cm.gray)
ax[1].set_title("Imagem melhorada - Histograma Equalizado")

fig.tight_layout()

plt.show()


