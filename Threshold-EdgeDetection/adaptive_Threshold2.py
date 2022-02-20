#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:01:18 2021

@author: burakzdd
"""

import cv2
import numpy as np
image =  cv2.imread('/home/burakzdd/Desktop/rapor5/bb8.jpg',0)
cv2.imshow('Input Image', image)


blurred = cv2.GaussianBlur(image, (5, 5), 0)
thresh = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
cv2.THRESH_BINARY_INV,blurred.max(),blurred.min())
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Input', closing)
cv2.waitKey(0)
cv2.destroyAllWindows()