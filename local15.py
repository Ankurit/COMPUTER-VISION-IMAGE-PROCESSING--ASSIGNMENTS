import cv2
import matplotlib.pyplot as plt 
import math
import numpy as np
image = cv2.imread("Fig0326(a)(embedded_square_noisy_512).tif")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# apply histogram equalization
print("[INFO] performing histogram equalization...")
gequalized = cv2.equalizeHist(gray)
# apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
print("[INFO] applying CLAHE...")
clahe = cv2.createCLAHE(clipLimit=256,tileGridSize=(3,3))
equalized = clahe.apply(gray)
gray1 = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
plt.imshow(gray1)
plt.show()
gray2 = cv2.cvtColor(gequalized, cv2.COLOR_GRAY2RGB)
plt.imshow( gray2)
plt.show()
gray3 = cv2.cvtColor(equalized, cv2.COLOR_GRAY2RGB)
plt.imshow(gray3)
plt.show()