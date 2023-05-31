import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import pyplot
import imageio
from PIL import Image 

# Carregando a imagem
img = cv2.imread('./images/bird.png',  -1)

# canal de cores
color = ('b','g','r')

for channel,col in enumerate(color):
    histr = cv2.calcHist([img],[channel],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.title('Histogram for color scale picture')
plt.show()

# Plotando a imagem original
img2 = Image.open("C:\\IMAGENS_UNIP\\bird.PNG")
pyplot.imshow(img2)

