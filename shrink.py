import numpy as np
import cv2
from math import sqrt,exp

from matplotlib import pyplot as plt

img = cv2.imread("Fig0220(a)(chronometer 3692x2812  2pt25 inch 1250 dpi).tif",0)
img = cv2.resize(img,(512,512))
x,y= img.shape[0],img.shape[1]

shrink_factor=2
new_img=np.zeros([round(x/shrink_factor),round(y/shrink_factor)])
x1,y1=new_img.shape[0],new_img.shape[1]
for i in range(0,x1):
  for j in range(0,y1):
    
    new_img[i,j]=img[i*2][j*2]

plt.subplot(1,2,1)
plt.imshow(img,cmap='gray')
plt.subplot(1,2,2)
plt.imshow(new_img,cmap='gray')
plt.show()