#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 18:46:41 2021
@author: burakzdd
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/burakzdd/Desktop/görüntü/nesne tespit/iha.jpg',0)
img2 = img.copy()
template = cv2.imread('/home/burakzdd/Desktop/görüntü/nesne tespit/iha2.jpg',0)
w, h = template.shape[::-1]

# Listede 6 yönteme de yer verilmiştir
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
for meth in methods:
    img = img2.copy()
    method = eval(meth)

    #şablon eşleme yöntemi eklenir
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# Eğer yöntem TM_SQDIFF veya TM_SQDIFF_NORMED ise minimum alınınr değilse max alınır
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img,top_left, bottom_right, 255, 2)
#görseller bastırılır 
    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()
    cv2.imshow('iha tespit',img)
cv2.waitKey(0)
cv2.destroyAllWindows()   
    