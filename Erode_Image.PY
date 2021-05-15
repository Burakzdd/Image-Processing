#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 21:33:56 2021

@author: burakzdd
"""
import cv2
import numpy as np

img = cv2.imread('/home/burakzdd/Desktop/rapor 6/coin.png',0)
cv2.imshow('Image',img)
otsu_threshold, img = cv2.threshold(img, 117, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU,)

cv2.imshow('Binary Image',img)

kernel = np.ones((11,11),np.uint8)
erode1 = cv2.erode(img,kernel,iterations = 1)
erode2 = cv2.erode(img,kernel,iterations = 2)
cv2.imshow('erode1 Image',erode1)
cv2.imshow('erode2 Image',erode2)
cv2.waitKey(0)
cv2.destroyAllWindows()


