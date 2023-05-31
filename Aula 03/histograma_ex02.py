import cv2
from matplotlib import pyplot
from matplotlib import pyplot as plt

# Carregando a imagem
gray_img = cv2.imread('./images/cameramen.png', cv2.IMREAD_GRAYSCALE)

# Obtendo e exibindo o histograma 
plt.hist(gray_img.ravel(),256,[0,256])
plt.title('Histogram for gray scale picture')
plt.show()

# Exibindo a imagem original
pyplot.imshow(gray_img,  cmap="gray")




