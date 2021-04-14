#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 00:01:20 2021
@author: burakzdd
"""
import cv2
img =  cv2.imread('/home/burakzdd/Desktop/rapor5/sw.jpg',0)

thresmean = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
thresgauss = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

cv2.imshow("Adaptive Thres Mean",thresmean)
cv2.imshow("Adaptive Thres Gauss",thresgauss)
cv2.waitKey(0)
cv2.destroyAllWindows()

