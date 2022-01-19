import cv2 
import numpy as np
import matplotlib.pyplot as plt

def bilinear_interpolation(img, scale):
    height,width =img.shape
    m,n = int(height),int(width*scale)
    new_img=np.zeros((m,n))
    for i in range(height):
        for j in range(width):
            p = i
            q = 2*j
            new_img[p,q] = int(img[i,j])
    for i in range(height):
        for j in range(width-1):
            new_img[i,((2*j)+1)] = int( (int(img[i,j])+int(img[i,j+1]))//2)
    
    new_img = new_img.astype(np.uint8)
    
    m,n = int(height*scale),int(width*scale)
    final_img = np.zeros((m,n))
    for i in range(int(m//2)):
        for j in range(n):
            p = 2*i
            q = j
            final_img[p,q] = new_img[i,j]
   
    for i in range(int(m/2-1)):
        for j in range(n):
            final_img[((2*i)+1),j] = int( (int(new_img[i,j])+int(new_img[i+1,j]))//2)
            
    final_img = final_img.astype(np.uint8)
    
    return final_img


img = cv2.imread('Fig0220(a)(chronometer 3692x2812  2pt25 inch 1250 dpi).tif')
img = cv2.resize(img,(256,256))
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
bilinear_img = bilinear_interpolation(gray_img, 2.0)
img2 = cv2.cvtColor(bilinear_img, cv2.COLOR_GRAY2RGB)
cv2.imshow("original",img)
cv2.imshow("zoomed",img2)
cv2.waitKey(0)