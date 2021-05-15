#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 18:18:42 2021

@author: burakzdd
"""

import cv2
import numpy as np
img = np.zeros((200,200,3), np.uint8)
cv2.rectangle (img,(20,20), (180,180), (100,100,100), -1)
cv2.rectangle (img,(40,40), (160,160), (150,150,150), -1)
cv2.rectangle (img,(60,60), (140,140), (200,200,200), -1)
cv2.rectangle (img,(80,80), (120,120), (256,256,256), -1)

dx = cv2.Sobel(img, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(img, cv2.CV_32F, 0, 1)

dikey = cv2.convertScaleAbs(dx)
yatay = cv2.convertScaleAbs(dy)
cv2.imshow("Dik kenarlar",dikey)
cv2.imshow("Yan kenarlar",yatay)

mag = cv2.addWeighted(dikey, 1, yatay, 1, -1)
cv2.imshow('Harita',mag)
cv2.waitKey(0)
cv2.destroyAllWindows()

