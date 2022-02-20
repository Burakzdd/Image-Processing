#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 21:42:18 2021

@author: burakzdd
"""

import cv2
import numpy as np


img = np.zeros((200,200,3), np.uint8)
cv2.rectangle (img,(20,20), (180,180), (100,100,100), -1)
cv2.rectangle (img,(40,40), (160,160), (150,150,150), -1)
cv2.rectangle (img,(60,60), (140,140), (200,200,200), -1)
cv2.rectangle (img,(80,80), (120,120), (256,256,256), -1)
cv2.imshow("kareler",img)

kernel = np.array([[1,1,1], [1,1,1], [1,1,1]]) / 9
mask = cv2.filter2D(img, -1, kernel,0)
cv2.imshow('gauss',mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
