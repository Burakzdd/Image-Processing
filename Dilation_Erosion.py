#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 21:28:20 2021

@author: burakzdd
"""

import cv2
import numpy as np

img = cv2.imread('/home/burakzdd/Desktop/rapor 6/dragon.jpeg', 0) 
otsu_threshold, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU,)
cv2.imshow('Binary Image',img)
 
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(img,kernel,iterations = 1)
erosion = cv2.erode(img,kernel,iterations = 1)

genisletmesiniri = dilation-img
asindirmasiniri = img-erosion

cv2.imshow('Sinirlar Dilation',genisletmesiniri)
cv2.imshow('Sinirlar Erosion',asindirmasiniri)
cv2.waitKey(0)
cv2.destroyAllWindows()
