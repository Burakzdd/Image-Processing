#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 20:06:50 2021

@author: burakzdd
"""

import cv2
import numpy as np

img = cv2.imread('/home/burakzdd/Desktop/rapor 6/burak1.png',0)
cv2.imshow("So", img)
#Numpy ile kernel matris tanımı
kernel = np.ones((5,5),np.uint8)
#Aşındırma işlemi
sonuc1 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
sonuc2 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Sonuc1", sonuc1)
cv2.imshow("Sonuc2", sonuc2)
cv2.waitKey(0)
