import cv2
import matplotlib.pyplot as plt 
import math
import numpy as np
img_third=cv2.imread("Fig0335(a)(ckt_board_saltpep_prob_pt05).tif")
image_rgb = cv2.cvtColor(img_third, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.show()
blur = cv2.boxFilter(img_third,-1,(3,3),normalize=True)
image_rgb = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.show()
median = cv2.medianBlur(src=img_third, ksize=3)
image_rgb = cv2.cvtColor(median, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.show()
