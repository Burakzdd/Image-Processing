#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 17:46:05 2021

@author: burakzdd
"""

import cv2
   
img = cv2.imread('/home/burakzdd/Desktop/hafta 3/marvel.jpg')
hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
 
cv2.imshow('Marvel Image',img)
cv2.imshow('HSV Marvel Image', hsvImg)
   
cv2.waitKey(0)
cv2.destroyAllWindows()

