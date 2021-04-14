#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 12:11:26 2021

@author: burakzdd
"""

import cv2
import numpy as np
img = np.zeros((200,200,3), np.uint8)
cv2.rectangle (img,(20,20), (180,180), (100,100,100), -1)
cv2.rectangle (img,(40,40), (160,160), (150,150,150), -1)
cv2.rectangle (img,(60,60), (140,140), (200,200,200), -1)
cv2.rectangle (img,(80,80), (120,120), (256,256,256), -1)

kernel_dikey = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
kernel_yatay = np.array([[1,2,1], [0,0,0], [-1,-2,-1]])

dikey = cv2.filter2D(img, -1, kernel_dikey) 
yatay = cv2.filter2D(img, -1, kernel_yatay)

cv2.imshow('Dikey',dikey)
cv2.imshow('Yatay ',yatay)
cv2.waitKey(0)
cv2.destroyAllWindows()

