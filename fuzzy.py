import numpy as np
from matplotlib.pyplot import imread
from matplotlib.pyplot import imsave

 import sys
sys.path.append('ee.tif')


def enhance_grayscale_8bit_image(image):
    """
    Parameters
    ----------
    image : numpy array, gray scale
        image to be manipulated.
    """
    dark_color = 0
    gray_color = 127
    bright_color = 255

    # The membership parameters can be modified, if the result
    # doesn't satisfy your expectations
    gray_membership_function = np.vectorize(
        triangular_membership_function(65, gray_color, 190))
    bright_membership_function = np.vectorize(
        sigma_membership_function(gray_color, 145))
    dark_membership_function = np.vectorize(
        inverse_sigma_membership_function(80, gray_color))

    dark_image_part = dark_membership_function(image)
    gray_image_part = gray_membership_function(image)
    bright_image_part = bright_membership_function(image)

    enhanced_image = (dark_image_part * dark_color +
                      gray_image_part * gray_color +
                      bright_image_part * bright_color) / \
        (dark_image_part + gray_image_part + bright_image_part)

    enhanced_image = enhanced_image.astype(np.uint8)
    return enhanced_image


import numpy as np


def triangular_membership_function(triangle_start, triangle_peak, triangle_end):
    def membership_function(parameter):
        if parameter < triangle_start:
            return 0

        if triangle_start <= parameter and parameter < triangle_peak:
            return (parameter - triangle_start) / (triangle_peak - triangle_start)

        if triangle_peak <= parameter and parameter < triangle_end:
            return 1 - (parameter - triangle_peak) / (triangle_end - triangle_peak)

        # triangle_end <= parameter
        return 0

    return membership_function


def sigma_membership_function(sigma_start, sigma_end):
    def membership_function(parameter):
        if parameter < sigma_start:
            return 0

        if sigma_start <= parameter and parameter < sigma_end:
            return (parameter - sigma_start) / (sigma_end - sigma_start)

        # sigma_end <= parameter
        return 1

    return membership_function


def inverse_sigma_membership_function(sigma_start, sigma_end):
    def membership_function(parameter):
        if parameter < sigma_start:
            return 1

        if sigma_start <= parameter and parameter < sigma_end:
            return 1 - (parameter - sigma_start) / (sigma_end - sigma_start)

        # sigma_end <= parameter
        return 0
    return membership_function

   
# The membership parameters can be modified, if the result
# doesn't satisfy your expectations
gray_membership_function = triangular_membership_function(65, 127, 180)
bright_membership_function = sigma_membership_function(127, 145)
dark_membership_function = inverse_sigma_membership_function(80, 127)

x = np.linspace(0, 255, 1000)
y1 = [gray_membership_function(param) for param in x]
y2 = [bright_membership_function(param) for param in x]
y3 = [dark_membership_function(param) for param in x]


fig, axs = plt.subplots(figsize=(25, 18))
axs.plot(x, y1, x, y2, x, y3)
axs.set_xlabel('Gray Values', fontsize=16)
axs.set_ylabel('Membership', fontsize=16)
axs.set_title("Membership Functions for 8 bit Images", fontsize=18)
axs.grid()

plt.annotate('Gray Membership Function', xy=(127, 1),
             xycoords='data',
             xytext=(-30, +30),
             textcoords='offset points',
             fontsize=16,
             arrowprops=dict(arrowstyle="->", 
             connectionstyle="arc3,rad=.2"))

plt.annotate('Dark Membership Function', xy=(30, 1),
             xycoords='data',
             xytext=(-30, +30),
             textcoords='offset points',
             fontsize=16,
             arrowprops=dict(arrowstyle="->", 
             connectionstyle="arc3,rad=.2"))

plt.annotate('Bright Membership Function', xy=(220, 1),
             xycoords='data',
             xytext=(-30, +30),
             textcoords='offset points',
             fontsize=16,
             arrowprops=dict(arrowstyle="->", 
             connectionstyle="arc3,rad=.2"))


plt.savefig("fuzzy_functions.svg")

plt.show()

def histogram_equalization(img_in):

# segregate color streams
    b,g,r = cv2.split(img_in)
    h_b, bin_b = np.histogram(b.flatten(), 256, [0, 256])
    h_g, bin_g = np.histogram(g.flatten(), 256, [0, 256])
    h_r, bin_r = np.histogram(r.flatten(), 256, [0, 256])
    
# calculate cdf    
    cdf_b = np.cumsum(h_b)  
    cdf_g = np.cumsum(h_g)
    cdf_r = np.cumsum(h_r)
    
# mask all pixels with value=0 and replace it with mean of the pixel values 
    cdf_m_b = np.ma.masked_equal(cdf_b,0)
    cdf_m_b = (cdf_m_b - cdf_m_b.min())*255/(cdf_m_b.max()-cdf_m_b.min())
    cdf_final_b = np.ma.filled(cdf_m_b,0).astype('uint8')
  
    cdf_m_g = np.ma.masked_equal(cdf_g,0)
    cdf_m_g = (cdf_m_g - cdf_m_g.min())*255/(cdf_m_g.max()-cdf_m_g.min())
    cdf_final_g = np.ma.filled(cdf_m_g,0).astype('uint8')
    
    cdf_m_r = np.ma.masked_equal(cdf_r,0)
    cdf_m_r = (cdf_m_r - cdf_m_r.min())*255/(cdf_m_r.max()-cdf_m_r.min())
    cdf_final_r = np.ma.filled(cdf_m_r,0).astype('uint8')
    
# merge the images in the three channels
    img_b = cdf_final_b[b]
    img_g = cdf_final_g[g]
    img_r = cdf_final_r[r]
  
    img_out = cv2.merge((img_b, img_g, img_r))
    
# validation
    equ_b = cv2.equalizeHist(b)
    equ_g = cv2.equalizeHist(g)
    equ_r = cv2.equalizeHist(r)
    
    equ = cv2.merge((equ_b, equ_g, equ_r))
    #print(equ)
    #cv2.imwrite('output_name.png', equ)
    return img_out


import numpy as np
from matplotlib.pyplot import imread
from matplotlib.pyplot import imsave

import sys
sys.path.append('src')


image = imread("ee.tif")
enhanced_image = enhance_grayscale_8bit_image(image)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.show()
equ = cv2.equalizeHist(image)

#display image
image_rgb1 = cv2.cvtColor(equ, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb1)
plt.show()

image_rgb1 = cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb1)
plt.show()