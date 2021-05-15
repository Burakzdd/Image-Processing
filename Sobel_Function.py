#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 12:46:59 2021

@author: burakzdd
"""

import cv2
import numpy as np

img = cv2.imread('/home/burakzdd/Desktop/hafta 3/sobelicin.png',0)
cv2.imshow('sobel',img)

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
cv2.imshow('x',sobelx)
cv2.imshow('y',sobely)

cv2.waitKey(0)
cv2.destroyAllWindows()
