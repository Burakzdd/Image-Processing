#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 09:30:35 2021

@author: burakzdd
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/burakzdd/Desktop/hafta 3/lena_noisy.png')
cv2.imshow('lena_noisy',img)

kernel = np.ones((3,3),np.float32)/9
dst = cv2.filter2D(img,-1,kernel)
cv2.imshow('smooth lena',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
