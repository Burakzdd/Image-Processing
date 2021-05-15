#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 14:45:53 2021

@author: burakzdd
"""
import cv2


img = cv2.imread('/home/burakzdd/Desktop/hafta 3/marvel.jpg')

b,g,r = cv2.split(img)


cv2.imshow("blue.png",b)
cv2.imshow("green.png",g)
cv2.imshow("red.png",r)

image = cv2.merge((b,g,r))
cv2.imshow('renkli', image)

cv2.waitKey(0)
cv2.destroyAllWindows()

