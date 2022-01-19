import cv2
import numpy as np
import pandas as pd
from PIL import Image
from numpy import asarray
from matplotlib import pyplot as plt
img = cv2.imread('Fig0221(a)(ctskull-256).tif')
plt.imshow(img)
plt.show()
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

level= 1  #input intensity level 
k=8-level
intensity_level=2**k
img_reduce = np.uint8(np.floor(np.double(img1)/intensity_level))
norm_img=cv2.normalize(img_reduce,None,0,255,norm_type=cv2.NORM_MINMAX)
img2 = cv2.cvtColor(norm_img, cv2.COLOR_GRAY2RGB)
plt.imshow(img2)
plt.show()