#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 22:43:01 2021

@author: burakzdd
"""
import numpy as np
import cv2

img = cv2.imread('/home/burakzdd/Desktop/hafta 3/castle.png',0)
cv2.imshow('image',img)

a = np.zeros((256,),dtype=np.float16)
b = np.zeros((256,),dtype=np.float16)

height,width=img.shape

for i in range(width):
    for j in range(height):
        g = img[j,i]
        a[g] = a[g]+1

tmp = 1.0/(height*width)

for i in range(256):
    for j in range(i+1):
        b[i] += a[j] * tmp;
    b[i] = round(b[i] * 255);

b=b.astype(np.uint8)

for i in range(width):
    for j in range(height):
        g = img[j,i]
        img[j,i]= b[g]

cv2.imshow('image2',img)
cv2.waitKey(0)
cv2.destroyAllWindows()