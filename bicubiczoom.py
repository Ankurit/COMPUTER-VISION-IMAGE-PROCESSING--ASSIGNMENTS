import numpy as np
import cv2
from math import sqrt,exp

from matplotlib import pyplot as plt

img = cv2.imread("Fig0220(a)(chronometer 3692x2812  2pt25 inch 1250 dpi).tif",0)
x,y=img.shape[0],img.shape[1]
bicubic_filter=np.array([[1,4,6,4,1],[4,16,24,16,4],[6,24,36,24,6],[4,16,24,16,4],[1,4,6,4,1]])*(1/64)

zoom_factor=2
new_img=np.zeros([x*zoom_factor,y*zoom_factor]).astype('uint8')
x1,y1=new_img.shape[0],new_img.shape[1]
for i in range(x):
  for j in range(y):
    new_img[zoom_factor*i][zoom_factor*j]=img[i][j]

n=cv2.filter2D(new_img,-1,bicubic_filter)

plt.subplot(1,2,1)
plt.title("original")
plt.imshow(img,cmap='gray')
plt.subplot(1,2,2)
plt.imshow(n,cmap='gray')
plt.title("shrink")
plt.show()